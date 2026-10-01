import os
import re
from html import escape

import yaml

DATA_FILE = "trajectory.yml"

TIMELINE_ENTRY = (
    '<div class="tl-entry {side}">\n'
    '    <div class="tl-marker"><span class="tl-dot"></span></div>\n'
    '    <div class="tl-content">\n'
    '        <time class="tl-date">{date}</time>\n'
    '        <h3 class="tl-title">{title}</h3>\n'
    '{text}'
    '{tags}'
    '    </div>\n'
    '</div>'
)

AWARD_ENTRY = (
    '<div class="tl-entry tl-aw-entry {side}" data-level="{level}">\n'
    '    <div class="tl-marker"><span class="tl-dot tl-aw-dot"></span></div>\n'
    '    <div class="tl-content">\n'
    '        <time class="tl-date">{date}</time>\n'
    '        <h3 class="tl-title tl-aw-event">{event}</h3>\n'
    '{note}'
    '        <div class="tl-entry-tags"><span class="tl-aw-rank">{rank}</span></div>\n'
    '    </div>\n'
    '</div>'
)


def _side(index):
    return "tl-left" if index % 2 == 0 else "tl-right"


def _sort_by_date(items):
    return sorted(
        items,
        key=lambda item: tuple(int(n) for n in re.findall(r"\d+", str(item.get("date", "")))),
        reverse=True,
    )


def _tags(tags, cls):
    if not tags:
        return ""
    spans = "".join(f'<span class="{cls}">{escape(str(tag))}</span>' for tag in tags)
    return f'        <div class="tl-entry-tags">{spans}</div>\n'


def _render_timeline(items):
    if not items:
        return ""
    entries = []
    for index, item in enumerate(_sort_by_date(items)):
        text = item.get("text")
        text_html = f'        <p class="tl-text">{escape(str(text))}</p>\n' if text else ""
        entries.append(
            TIMELINE_ENTRY.format(
                side=_side(index),
                date=escape(str(item.get("date", ""))),
                title=escape(str(item.get("title", ""))),
                text=text_html,
                tags=_tags(item.get("tags"), "tl-entry-tag"),
            )
        )
    return '<div class="tl-container">\n' + "\n".join(entries) + "\n</div>"


def _render_awards(items):
    if not items:
        return ""
    entries = []
    for index, item in enumerate(_sort_by_date(items)):
        note = item.get("note")
        note_html = f'        <p class="tl-text tl-aw-note">{escape(str(note))}</p>\n' if note else ""
        entries.append(
            AWARD_ENTRY.format(
                side=_side(index),
                level=escape(str(item.get("level", "n"))),
                date=escape(str(item.get("date", ""))),
                event=escape(str(item.get("event", ""))),
                note=note_html,
                rank=escape(str(item.get("rank", ""))),
            )
        )
    return '<div class="tl-container tl-awards">\n' + "\n".join(entries) + "\n</div>"


def on_page_markdown(markdown, *, page, config, files, **kwargs):
    if "{{ TIMELINE }}" not in markdown and "{{ AWARDS }}" not in markdown:
        return markdown

    data_path = os.path.join(config["docs_dir"], DATA_FILE)
    with open(data_path, encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    markdown = markdown.replace("{{ TIMELINE }}", _render_timeline(data.get("timeline")))
    markdown = markdown.replace("{{ AWARDS }}", _render_awards(data.get("awards")))
    return markdown
