"""Local embedding and semantic search over promoted endpoint DB chunks."""

from __future__ import annotations

import hashlib
import json
import math
import sqlite3
from functools import lru_cache
from pathlib import Path

from app.models import SearchResult, SemanticChunkCandidate
from app.settings import settings
from services.intake import semantic_ready_chunks


def _connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def _endpoint_db_path(target_pou: str) -> Path:
    return settings.project_root / "var" / "db" / f"{target_pou}.db"


def _init_vector_table(path: Path) -> None:
    with _connect(path) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS semantic_index (
                chunk_id TEXT PRIMARY KEY,
                intake_id TEXT NOT NULL,
                target_pou TEXT NOT NULL,
                source_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                embedding_json TEXT NOT NULL,
                embedding_model TEXT NOT NULL,
                embedding_dim INTEGER NOT NULL
            )
            """
        )
        conn.commit()


@lru_cache(maxsize=1)
def _sentence_transformer():
    if settings.embedding_mode != "sentence-transformers":
        return None
    try:
        from sentence_transformers import SentenceTransformer  # type: ignore
    except ImportError:
        return None
    return SentenceTransformer(settings.embedding_model)


def _hash_embed(text: str, dim: int) -> list[float]:
    vector = [0.0] * dim
    for token in text.lower().split():
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:2], "big") % dim
        sign = 1.0 if digest[2] % 2 == 0 else -1.0
        vector[index] += sign
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def embed_text(text: str) -> list[float]:
    model = _sentence_transformer()
    if model is not None:
        vector = model.encode(text, normalize_embeddings=True).tolist()
        return [float(value) for value in vector]
    return _hash_embed(text, settings.embedding_dim)


def sync_semantic_index(target_pou: str | None = None, limit: int = 100) -> dict[str, object]:
    candidates = semantic_ready_chunks(target_pou=target_pou, limit=limit)
    indexed = 0
    touched: dict[str, int] = {}
    for candidate in candidates:
        db_path = _endpoint_db_path(candidate.target_pou)
        _init_vector_table(db_path)
        vector = embed_text(candidate.embedding_input)
        with _connect(db_path) as conn:
            conn.execute(
                """
                INSERT INTO semantic_index (
                    chunk_id, intake_id, target_pou, source_id, chunk_index,
                    embedding_json, embedding_model, embedding_dim
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(chunk_id) DO UPDATE SET
                    embedding_json=excluded.embedding_json,
                    embedding_model=excluded.embedding_model,
                    embedding_dim=excluded.embedding_dim
                """,
                (
                    candidate.chunk_id,
                    candidate.intake_id,
                    candidate.target_pou,
                    candidate.source_id,
                    candidate.chunk_index,
                    json.dumps(vector),
                    settings.embedding_model,
                    len(vector),
                ),
            )
            conn.commit()
        indexed += 1
        touched[candidate.target_pou] = touched.get(candidate.target_pou, 0) + 1
    return {
        "indexed_chunks": indexed,
        "embedding_model": settings.embedding_model,
        "embedding_mode": settings.embedding_mode,
        "by_pou": touched,
    }


def _cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    return sum(a * b for a, b in zip(left, right))


def semantic_search(query: str, target_pou: str | None = None, limit: int = 5) -> list[SearchResult]:
    query_vec = embed_text(query)
    results: list[SearchResult] = []
    db_dir = settings.project_root / "var" / "db"
    if not db_dir.exists():
        return []
    db_paths = [_endpoint_db_path(target_pou)] if target_pou else sorted(db_dir.glob("*.db"))
    for db_path in db_paths:
        if not db_path.exists():
            continue
        _init_vector_table(db_path)
        with _connect(db_path) as conn:
            rows = conn.execute(
                """
                SELECT
                    s.chunk_id,
                    s.intake_id,
                    s.chunk_index,
                    s.source_id,
                    s.embedding_json,
                    c.chunk_text
                FROM semantic_index AS s
                JOIN index_chunks AS c
                  ON c.chunk_id = s.chunk_id
                """
            ).fetchall()
        for row in rows:
            score = _cosine_similarity(query_vec, json.loads(row["embedding_json"]))
            if score <= 0:
                continue
            results.append(
                SearchResult(
                    target_pou=db_path.stem,
                    intake_id=row["intake_id"],
                    chunk_id=row["chunk_id"],
                    chunk_index=row["chunk_index"],
                    chunk_text=row["chunk_text"],
                    source_id=row["source_id"],
                    score=int(score * 1000),
                )
            )
    results.sort(key=lambda item: (-item.score, item.target_pou, item.chunk_index))
    return results[:limit]
