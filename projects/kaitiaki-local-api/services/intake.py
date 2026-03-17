"""Local-first intake, scrub, staging, and promotion flow."""

from __future__ import annotations

import json
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.models import IntakeRequest, SearchResult, SemanticChunkCandidate
from app.settings import settings
from services.guardian import guardian_intake_decision


KEEP_META_KEYS = {
    "title",
    "source_url",
    "language",
    "content_type",
    "author",
    "published_at",
    "tags",
    "notes",
}


@dataclass
class IntakeResult:
    intake_id: str
    target_pou: str
    allowed: bool
    cleaned: bool
    meta_scrubbed: bool
    ready_for_indexing: bool
    promoted: bool
    stage_db: str
    endpoint_db: str | None


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _connect(path: Path) -> sqlite3.Connection:
    _ensure_parent(path)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def _init_stage_db(path: Path) -> None:
    with _connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS intake_stage (
                intake_id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                target_pou TEXT NOT NULL,
                tapu_level TEXT NOT NULL,
                content_raw TEXT NOT NULL,
                content_clean TEXT NOT NULL,
                metadata_json TEXT NOT NULL,
                cleaned INTEGER NOT NULL,
                meta_scrubbed INTEGER NOT NULL,
                ready_for_indexing INTEGER NOT NULL,
                promoted INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        conn.commit()


def _init_endpoint_db(path: Path) -> None:
    with _connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS intake_records (
                intake_id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                tapu_level TEXT NOT NULL,
                content_clean TEXT NOT NULL,
                metadata_json TEXT NOT NULL,
                chunk_count INTEGER NOT NULL
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS index_chunks (
                chunk_id TEXT PRIMARY KEY,
                intake_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                chunk_text TEXT NOT NULL
            )
            """
        )
        conn.commit()


def _scrub_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    scrubbed = {key: value for key, value in metadata.items() if key in KEEP_META_KEYS}
    if "author_email" in metadata:
        scrubbed["meta_scrub_note"] = "sensitive metadata removed"
    return scrubbed


def _clean_content(text: str) -> str:
    cleaned = text.replace("\u00a0", " ")
    cleaned = "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    return cleaned.strip()


def _chunk_content(text: str, chunk_size: int = 400) -> list[str]:
    words = text.split()
    if not words:
        return []
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for word in words:
        projected = current_len + len(word) + (1 if current else 0)
        if projected > chunk_size and current:
            chunks.append(" ".join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len = projected
    if current:
        chunks.append(" ".join(current))
    return chunks


def _stage_db_path() -> Path:
    return settings.project_root / "var" / "state" / "intake-stage.db"


def _endpoint_db_path(target_pou: str) -> Path:
    return settings.project_root / "var" / "db" / f"{target_pou}.db"


def _endpoint_db_paths(target_pou: str | None = None) -> list[Path]:
    if target_pou:
        return [_endpoint_db_path(target_pou)]
    db_dir = settings.project_root / "var" / "db"
    if not db_dir.exists():
        return []
    return sorted(db_dir.glob("*.db"))


def ingest_intake(request: IntakeRequest) -> IntakeResult:
    decision = guardian_intake_decision(request.target_pou, request.tapu_level)
    if not decision["allowed"]:
        return IntakeResult(
            intake_id="blocked",
            target_pou=request.target_pou,
            allowed=False,
            cleaned=False,
            meta_scrubbed=False,
            ready_for_indexing=False,
            promoted=False,
            stage_db=str(_stage_db_path()),
            endpoint_db=None,
        )

    cleaned_content = _clean_content(request.content)
    scrubbed_meta = _scrub_metadata(request.metadata)
    intake_id = str(uuid.uuid4())
    stage_db = _stage_db_path()
    endpoint_db = _endpoint_db_path(request.target_pou)

    _init_stage_db(stage_db)
    _init_endpoint_db(endpoint_db)

    with _connect(stage_db) as conn:
        conn.execute(
            """
            INSERT INTO intake_stage (
                intake_id, source_id, target_pou, tapu_level, content_raw, content_clean,
                metadata_json, cleaned, meta_scrubbed, ready_for_indexing, promoted
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
            """,
            (
                intake_id,
                request.source_id,
                request.target_pou,
                request.tapu_level,
                request.content,
                cleaned_content,
                json.dumps(scrubbed_meta, ensure_ascii=False),
                1,
                1,
                1,
            ),
        )
        conn.commit()

    chunks = _chunk_content(cleaned_content)
    with _connect(endpoint_db) as conn:
        conn.execute(
            """
            INSERT INTO intake_records (
                intake_id, source_id, tapu_level, content_clean, metadata_json, chunk_count
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                intake_id,
                request.source_id,
                request.tapu_level,
                cleaned_content,
                json.dumps(scrubbed_meta, ensure_ascii=False),
                len(chunks),
            ),
        )
        conn.executemany(
            """
            INSERT INTO index_chunks (chunk_id, intake_id, chunk_index, chunk_text)
            VALUES (?, ?, ?, ?)
            """,
            [
                (f"{intake_id}:{idx}", intake_id, idx, chunk)
                for idx, chunk in enumerate(chunks)
            ],
        )
        conn.commit()

    with _connect(stage_db) as conn:
        conn.execute(
            "UPDATE intake_stage SET promoted = 1 WHERE intake_id = ?",
            (intake_id,),
        )
        conn.commit()

    return IntakeResult(
        intake_id=intake_id,
        target_pou=request.target_pou,
        allowed=True,
        cleaned=True,
        meta_scrubbed=True,
        ready_for_indexing=True,
        promoted=True,
        stage_db=str(stage_db),
        endpoint_db=str(endpoint_db),
    )


def fetch_staged_intake(intake_id: str) -> dict[str, Any] | None:
    stage_db = _stage_db_path()
    if not stage_db.exists():
        return None
    with _connect(stage_db) as conn:
        row = conn.execute(
            "SELECT * FROM intake_stage WHERE intake_id = ?",
            (intake_id,),
        ).fetchone()
    if row is None:
        return None
    data = dict(row)
    data["metadata_json"] = json.loads(data["metadata_json"])
    return data


def search_intake(query: str, target_pou: str | None = None, limit: int = 5) -> list[SearchResult]:
    needle = query.strip().lower()
    if not needle:
        return []

    results: list[SearchResult] = []
    for db_path in _endpoint_db_paths(target_pou):
        with _connect(db_path) as conn:
            rows = conn.execute(
                """
                SELECT
                    c.chunk_id,
                    c.intake_id,
                    c.chunk_index,
                    c.chunk_text,
                    r.source_id
                FROM index_chunks AS c
                JOIN intake_records AS r
                  ON r.intake_id = c.intake_id
                """
            ).fetchall()

        for row in rows:
            haystack = str(row["chunk_text"]).lower()
            occurrences = haystack.count(needle)
            if occurrences <= 0:
                continue
            results.append(
                SearchResult(
                    target_pou=db_path.stem,
                    intake_id=row["intake_id"],
                    chunk_id=row["chunk_id"],
                    chunk_index=row["chunk_index"],
                    chunk_text=row["chunk_text"],
                    source_id=row["source_id"],
                    score=occurrences,
                )
            )

    results.sort(key=lambda item: (-item.score, item.target_pou, item.chunk_index))
    return results[:limit]


def intake_summary() -> dict[str, Any]:
    stage_db = _stage_db_path()
    stage_count = 0
    if stage_db.exists():
        with _connect(stage_db) as conn:
            row = conn.execute("SELECT COUNT(*) AS count FROM intake_stage").fetchone()
        stage_count = int(row["count"]) if row is not None else 0

    endpoint_counts: dict[str, int] = {}
    for db_path in _endpoint_db_paths():
        with _connect(db_path) as conn:
            row = conn.execute("SELECT COUNT(*) AS count FROM intake_records").fetchone()
        endpoint_counts[db_path.stem] = int(row["count"]) if row is not None else 0

    return {
        "stage_db": str(stage_db),
        "staged_records": stage_count,
        "endpoint_counts": endpoint_counts,
    }


def semantic_ready_chunks(target_pou: str | None = None, limit: int = 20) -> list[SemanticChunkCandidate]:
    results: list[SemanticChunkCandidate] = []
    for db_path in _endpoint_db_paths(target_pou):
        with _connect(db_path) as conn:
            rows = conn.execute(
                """
                SELECT
                    c.chunk_id,
                    c.intake_id,
                    c.chunk_index,
                    c.chunk_text,
                    r.source_id
                FROM index_chunks AS c
                JOIN intake_records AS r
                  ON r.intake_id = c.intake_id
                ORDER BY c.intake_id, c.chunk_index
                """
            ).fetchall()
        for row in rows:
            chunk_text = str(row["chunk_text"]).strip()
            if len(chunk_text) < 12:
                continue
            results.append(
                SemanticChunkCandidate(
                    target_pou=db_path.stem,
                    intake_id=row["intake_id"],
                    chunk_id=row["chunk_id"],
                    chunk_index=row["chunk_index"],
                    source_id=row["source_id"],
                    embedding_input=chunk_text,
                )
            )
    return results[:limit]
