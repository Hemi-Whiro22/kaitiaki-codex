"""Type-aware local extraction into a text-centered intake representation."""

from __future__ import annotations

import json
from html.parser import HTMLParser


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.parts.append(text)

    def as_text(self) -> str:
        return "\n".join(self.parts)


def detect_source_type(filename: str | None, content_type: str | None) -> str:
    name = (filename or "").lower()
    ctype = (content_type or "").lower()
    if name.endswith(".md") or "markdown" in ctype:
        return "markdown"
    if name.endswith(".json") or "json" in ctype:
        return "json"
    if name.endswith(".html") or name.endswith(".htm") or "html" in ctype:
        return "html"
    if name.endswith(".txt") or "text/plain" in ctype:
        return "text"
    return "text"


def extract_text_content(raw_bytes: bytes, source_type: str) -> str:
    text = raw_bytes.decode("utf-8", errors="replace")
    if source_type == "json":
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            return text
        return json.dumps(parsed, ensure_ascii=False, indent=2)
    if source_type == "html":
        parser = _HTMLTextExtractor()
        parser.feed(text)
        return parser.as_text()
    return text
