import hashlib
import logging
import posixpath
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

from mkdocs.structure.files import File
from mkdocs.utils import get_relative_url
from PIL import Image, ImageOps, __version__ as pillow_version

log = logging.getLogger("mkdocs.hooks.images")
_images = {}


def _prepare_image(source, cache_dir, *, favicon=False):
    content = source.read_bytes()
    digest = hashlib.sha256(content + pillow_version.encode()).hexdigest()
    suffix = ".png" if favicon else ".webp"
    cached = cache_dir / (digest + suffix)
    with Image.open(source) as image:
        if getattr(image, "is_animated", False):
            return image.size, None
        image = ImageOps.exif_transpose(image)
        if favicon:
            image = image.convert("RGBA")
            image.thumbnail((64, 64), Image.Resampling.LANCZOS)
        else:
            mode = "RGBA" if "A" in image.getbands() or "transparency" in image.info else "RGB"
            image = image.convert(mode)
        size = image.size
        if not cached.exists():
            temporary = cached.with_suffix(cached.suffix + ".tmp")
            if favicon:
                image.save(temporary, format="PNG", optimize=True)
            else:
                metadata = {key: image.info[key] for key in ("icc_profile", "exif") if key in image.info}
                image.save(temporary, format="WEBP", lossless=True, exact=True, method=6, **metadata)
            temporary.replace(cached)
    if cached.stat().st_size < len(content) * 0.95:
        return size, cached
    return size, None


def on_files(files, *, config, **kwargs):
    _images.clear()
    cache_dir = Path(config.config_file_path).parent / ".cache" / "image-variants-v1"
    cache_dir.mkdir(parents=True, exist_ok=True)
    favicon = str(config.theme.get("favicon", "")).lstrip("/")
    original_bytes = optimized_bytes = variants = 0
    for file in list(files):
        if Path(file.src_uri).suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        source = Path(file.abs_src_path)
        if not source.is_relative_to(Path(config.docs_dir)):
            continue
        size, cached = _prepare_image(source, cache_dir, favicon=file.src_uri == favicon)
        optimized_uri = file.src_uri
        if cached is not None:
            optimized_uri = file.src_uri if file.src_uri == favicon else file.src_uri + ".webp"
            if optimized_uri == file.src_uri:
                files.remove(file)
            elif files.get_file_from_path(optimized_uri) is not None:
                _images[file.src_uri] = (size, file.src_uri)
                continue
            files.append(File.generated(config, optimized_uri, abs_src_path=str(cached)))
            variants += 1
            original_bytes += source.stat().st_size
            optimized_bytes += cached.stat().st_size
        _images[file.src_uri] = (size, optimized_uri)
    logo = str(config.theme.get("logo", ""))
    if logo.lstrip("/") in _images:
        optimized_uri = _images[logo.lstrip("/")][1]
        config.theme["logo"] = ("/" if logo.startswith("/") else "") + optimized_uri
    log.info(
        "Image optimization: %d variants, %.2f MiB -> %.2f MiB (original URLs preserved)",
        variants, original_bytes / 1048576, optimized_bytes / 1048576,
    )
    return files


class _ImageParser(HTMLParser):
    def __init__(self, content, page):
        super().__init__(convert_charrefs=False)
        self.content = content
        self.page = page
        self.patches = []
        self.image_count = 0
        self.line_offsets = [0]
        for line in content.splitlines(keepends=True):
            self.line_offsets.append(self.line_offsets[-1] + len(line))

    def handle_starttag(self, tag, attrs):
        if tag != "img":
            return
        attrs = dict(attrs)
        self.image_count += 1
        first = self.image_count == 1 or self.page.meta.get("home", False)
        attrs.setdefault("loading", "eager" if first else "lazy")
        attrs.setdefault("decoding", "async")
        url = urlsplit(attrs.get("src") or "")
        if not url.scheme and not url.netloc and url.path:
            path = unquote(url.path)
            uri = posixpath.normpath(
                path.lstrip("/") if path.startswith("/")
                else posixpath.join(posixpath.dirname(self.page.url), path)
            )
            if uri in _images:
                (width, height), optimized_uri = _images[uri]
                if "width" not in attrs and "height" not in attrs:
                    attrs.update(width=str(width), height=str(height))
                if "srcset" not in attrs:
                    path = "/" + optimized_uri if url.path.startswith("/") else get_relative_url(optimized_uri, self.page.url)
                    attrs["src"] = urlunsplit(("", "", path, url.query, url.fragment))
        rendered = "<img" + "".join(
            " " + name + ("" if value is None else '="' + escape(value, quote=True) + '"')
            for name, value in attrs.items()
        ) + ">"
        line, column = self.getpos()
        start = self.line_offsets[line - 1] + column
        self.patches.append((start, start + len(self.get_starttag_text()), rendered))

    handle_startendtag = handle_starttag


def on_page_content(html, *, page, **kwargs):
    parser = _ImageParser(html, page)
    parser.feed(html)
    for start, end, rendered in reversed(parser.patches):
        html = html[:start] + rendered + html[end:]
    return html
