"""Type-aware local extraction into a text-centered intake representation."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


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


@dataclass
class ExtractedContent:
    text: str
    kind: str
    linked_assets: list[str]


TEXT_SOURCE_TYPES = {"text", "markdown", "json", "html", "chat_export_html", "chat_export_json"}
ASSET_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".mp3",
    ".wav",
    ".m4a",
    ".ogg",
    ".mp4",
    ".mov",
}


def detect_source_type(filename: str | None, content_type: str | None) -> str:
    name = (filename or "").lower()
    ctype = (content_type or "").lower()
    if name == "chat.html":
        return "chat_export_html"
    if name.startswith("conversations") and name.endswith(".json"):
        return "chat_export_json"
    if name.endswith(".md") or "markdown" in ctype:
        return "markdown"
    if name.endswith(".json") or "json" in ctype:
        return "json"
    if name.endswith(".html") or name.endswith(".htm") or "html" in ctype:
        return "html"
    if name.endswith(".txt") or "text/plain" in ctype:
        return "text"
    return "text"


def _flatten_chat_mapping(conversation: dict[str, Any], assets: dict[str, str]) -> tuple[str, list[str]]:
    mapping = conversation.get("mapping", {})
    current_node = conversation.get("current_node")
    messages: list[tuple[str, list[str]]] = []
    linked_assets: list[str] = []

    while current_node is not None:
        node = mapping.get(current_node) or {}
        message = node.get("message") or {}
        content = message.get("content") or {}
        parts = content.get("parts") or []
        metadata = message.get("metadata") or {}
        author = ((message.get("author") or {}).get("role")) or "unknown"
        if parts and (author != "system" or metadata.get("is_user_system_message")):
            label = "ChatGPT" if author in {"assistant", "tool"} else author
            message_parts: list[str] = []
            for part in parts:
                if isinstance(part, str) and part.strip():
                    message_parts.append(part.strip())
                elif isinstance(part, dict):
                    part_type = part.get("content_type")
                    if part_type == "audio_transcription" and part.get("text"):
                        message_parts.append(f"[Transcript] {part['text']}")
                    else:
                        asset_pointer = part.get("asset_pointer")
                        if asset_pointer and asset_pointer in assets:
                            linked_assets.append(assets[asset_pointer])
                            message_parts.append(f"[File] {assets[asset_pointer]}")
            if message_parts:
                messages.append((label, message_parts))
        current_node = node.get("parent")

    lines: list[str] = []
    title = str(conversation.get("title") or "Untitled conversation").strip()
    lines.append(f"# {title}")
    for label, message_parts in reversed(messages):
        lines.append(f"[{label}]")
        lines.extend(message_parts)
        lines.append("")
    return "\n".join(line for line in lines if line is not None).strip(), linked_assets


def _extract_chat_export_html(text: str) -> ExtractedContent:
    json_marker = "var jsonData = "
    assets_marker = "var assetsJson = "
    json_start = text.find(json_marker)
    assets_start = text.find(assets_marker)
    if json_start < 0 or assets_start < 0 or assets_start <= json_start:
        parser = _HTMLTextExtractor()
        parser.feed(text)
        return ExtractedContent(text=parser.as_text(), kind="html", linked_assets=[])

    raw_json = text[json_start + len(json_marker) : assets_start].rstrip(" ;\n")
    assets_end = text.find("function getConversationMessages", assets_start)
    raw_assets = text[assets_start + len(assets_marker) : assets_end].rstrip(" ;\n")

    try:
        conversations = json.loads(raw_json)
        assets = json.loads(raw_assets)
    except json.JSONDecodeError:
        parser = _HTMLTextExtractor()
        parser.feed(text)
        return ExtractedContent(text=parser.as_text(), kind="html", linked_assets=[])

    blocks: list[str] = []
    linked_assets: list[str] = []
    for conversation in conversations:
        block, conversation_assets = _flatten_chat_mapping(conversation, assets)
        if block:
            blocks.append(block)
        linked_assets.extend(conversation_assets)

    return ExtractedContent(
        text="\n\n".join(blocks).strip(),
        kind="chat_export_html",
        linked_assets=sorted(set(linked_assets)),
    )


def _extract_chat_export_json(text: str) -> ExtractedContent:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return ExtractedContent(text=text, kind="json", linked_assets=[])

    conversations = payload if isinstance(payload, list) else [payload]
    blocks: list[str] = []
    for item in conversations:
        if isinstance(item, dict) and "mapping" in item:
            block, _ = _flatten_chat_mapping(item, {})
            if block:
                blocks.append(block)

    if blocks:
        return ExtractedContent(
            text="\n\n".join(blocks).strip(),
            kind="chat_export_json",
            linked_assets=[],
        )
    return ExtractedContent(
        text=json.dumps(payload, ensure_ascii=False, indent=2),
        kind="json",
        linked_assets=[],
    )


def extract_content_payload(raw_bytes: bytes, source_type: str) -> ExtractedContent:
    text = raw_bytes.decode("utf-8", errors="replace")
    if source_type == "chat_export_html":
        return _extract_chat_export_html(text)
    if source_type == "chat_export_json":
        return _extract_chat_export_json(text)
    if source_type == "json":
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            return ExtractedContent(text=text, kind="json", linked_assets=[])
        return ExtractedContent(
            text=json.dumps(parsed, ensure_ascii=False, indent=2),
            kind="json",
            linked_assets=[],
        )
    if source_type == "html":
        parser = _HTMLTextExtractor()
        parser.feed(text)
        return ExtractedContent(text=parser.as_text(), kind="html", linked_assets=[])
    return ExtractedContent(text=text, kind=source_type, linked_assets=[])


def extract_text_content(raw_bytes: bytes, source_type: str) -> str:
    return extract_content_payload(raw_bytes, source_type).text


def classify_archive_file(path: Path) -> str:
    if path.suffix.lower() in ASSET_EXTENSIONS:
        return "asset"
    source_type = detect_source_type(path.name, None)
    if source_type in TEXT_SOURCE_TYPES:
        return "text"
    return "other"


def infer_archive_kind(folder_path: Path) -> str:
    names = {path.name.lower() for path in folder_path.iterdir() if path.is_file()}
    if "chat.html" in names:
        return "chatgpt_export_folder"
    if any(name.startswith("conversations") and name.endswith(".json") for name in names):
        return "conversation_json_archive"
    return "mixed_archive"


def scan_archive_folder(folder_path: str, max_candidates: int = 20) -> dict[str, Any]:
    root = Path(folder_path).expanduser().resolve()
    file_counts = {"text": 0, "asset": 0, "other": 0}
    text_candidates: list[str] = []
    asset_candidates: list[str] = []

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        kind = classify_archive_file(path)
        file_counts[kind] += 1
        rel = str(path.relative_to(root))
        if kind == "text" and len(text_candidates) < max_candidates:
            text_candidates.append(rel)
        elif kind == "asset" and len(asset_candidates) < max_candidates:
            asset_candidates.append(rel)

    return {
        "folder_path": str(root),
        "archive_kind": infer_archive_kind(root),
        "file_counts": file_counts,
        "text_candidates": text_candidates,
        "asset_candidates": asset_candidates,
    }
