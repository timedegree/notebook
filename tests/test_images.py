import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from PIL import Image

from hooks import images


class ImageHookTests(unittest.TestCase):
    def setUp(self):
        images._images.clear()
        self.page = SimpleNamespace(url="wp/2024/test/", meta={})
        images._images["assets/shot.png"] = ((1200, 800), "assets/shot.png.webp")

    def render(self, html):
        return images.on_page_content(html, page=self.page)

    def test_relative_urls_dimensions_and_loading(self):
        rendered = self.render('<p>before</p>\n<img src="../../../assets/shot.png">\n<img src="../../../assets/shot.png">')
        self.assertTrue(rendered.startswith("<p>before</p>\n"))
        self.assertIn('src="../../../assets/shot.png.webp"', rendered)
        self.assertIn('width="1200" height="800"', rendered)
        self.assertEqual(rendered.count('loading="eager"'), 1)
        self.assertEqual(rendered.count('loading="lazy"'), 1)

    def test_explicit_attributes_are_preserved(self):
        rendered = self.render('<img src="/assets/shot.png?x=1&amp;y=2#figure" width="170px" height="170px" loading="lazy" decoding="sync" />')
        self.assertIn('src="/assets/shot.png.webp?x=1&amp;y=2#figure"', rendered)
        self.assertIn('width="170px" height="170px"', rendered)
        self.assertIn('loading="lazy" decoding="sync"', rendered)

    def test_external_and_srcset_urls_are_preserved(self):
        rendered = self.render('<img src="https://example.com/a.png"><img src="/assets/shot.png" srcset="/assets/shot.png 2x">')
        self.assertIn('src="https://example.com/a.png"', rendered)
        self.assertIn('src="/assets/shot.png" srcset="/assets/shot.png 2x"', rendered)

    def test_home_images_remain_eager(self):
        self.page.meta = {"home": True}
        rendered = self.render('<img src="/assets/shot.png"><img src="/assets/shot.png">')
        self.assertNotIn('loading="lazy"', rendered)

    def test_multiline_tags_and_script_content(self):
        html = '<script>const x = "<img>";</script>\n<img\n src="/assets/shot.png">\n<p>after</p>'
        rendered = self.render(html)
        self.assertTrue(rendered.startswith('<script>const x = "<img>";</script>\n'))
        self.assertTrue(rendered.endswith("\n<p>after</p>"))

    def test_lossless_variant_and_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "shot.png"
            original = Image.new("RGBA", (300, 200), (31, 77, 121, 127))
            original.save(source, compress_level=0)
            size, cached = images._prepare_image(source, root)
            self.assertEqual(size, original.size)
            self.assertIsNotNone(cached)
            with Image.open(cached) as optimized:
                self.assertEqual(optimized.convert("RGBA").tobytes(), original.tobytes())
            modified = cached.stat().st_mtime_ns
            self.assertEqual(images._prepare_image(source, root)[1], cached)
            self.assertEqual(cached.stat().st_mtime_ns, modified)

    def test_favicon_is_resized(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "favicon.png"
            Image.new("RGBA", (512, 256), (31, 77, 121, 255)).save(source, compress_level=0)
            size, cached = images._prepare_image(source, root, favicon=True)
            self.assertEqual(size, (64, 32))
            self.assertIsNotNone(cached)

    def test_jpeg_orientation_and_color_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "photo.jpg"
            original = Image.new("RGB", (300, 200), (31, 77, 121))
            exif = Image.Exif()
            exif[274] = 6
            original.save(source, exif=exif, icc_profile=b"test-profile")
            size, cached = images._prepare_image(source, root)
            self.assertEqual(size, (200, 300))
            self.assertIsNotNone(cached)
            with Image.open(source) as jpeg, Image.open(cached) as optimized:
                self.assertEqual(optimized.tobytes(), images.ImageOps.exif_transpose(jpeg).tobytes())
                self.assertEqual(optimized.info["icc_profile"], b"test-profile")
                self.assertNotIn(274, optimized.getexif())


if __name__ == "__main__":
    unittest.main()
