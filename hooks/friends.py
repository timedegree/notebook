import os
import posixpath
from html import escape

import yaml

DATA_FILE = "links.yml"

GROUP_TEMPLATE = (
    '<h2 class="flink-group-title">{title}</h2>\n\n'
    '<div class="flink-list">\n{items}\n</div>'
)

ITEM_TEMPLATE = (
    '<div class="flink-list-item">\n'
    '    <a{attrs}>\n'
    '        <div class="flink-item-icon">\n'
    '            <img src="{avatar}" alt="">\n'
    '        </div>\n'
    '        <div class="flink-item-name heti-skip">{name}</div>\n'
    '        <div class="flink-item-desc">{desc}</div>\n'
    '    </a>\n'
    '</div>'
)


def _avatar_url(src, page):
    if "://" in src or src.startswith("data:"):
        return src
    return posixpath.relpath(src.lstrip("/"), posixpath.dirname(page.url) or ".")


def _render(groups, page):
    blocks = []
    for group in groups or []:
        items = []
        for friend in group.get("items", []) or []:
            url = str(friend.get("url", "") or "").strip()
            name = escape(str(friend.get("name", "")))
            if url:
                attrs = f' href="{escape(url)}" title="{name}" target="_blank" rel="noopener"'
            else:
                attrs = f' title="{name}" aria-disabled="true"'
            items.append(
                ITEM_TEMPLATE.format(
                    attrs=attrs,
                    name=name,
                    avatar=escape(_avatar_url(str(friend.get("avatar", "")), page)),
                    desc=escape(str(friend.get("desc", ""))),
                )
            )
        blocks.append(
            GROUP_TEMPLATE.format(
                title=escape(str(group.get("title", ""))),
                items="\n".join(items),
            )
        )
    return "\n\n".join(blocks)


def on_page_markdown(markdown, *, page, config, files, **kwargs):
    if "{{ FRIENDS }}" not in markdown:
        return markdown

    data_path = os.path.join(config["docs_dir"], DATA_FILE)
    with open(data_path, encoding="utf-8") as file:
        groups = yaml.safe_load(file) or []

    return markdown.replace("{{ FRIENDS }}", _render(groups, page))
