"""Shared request and response models for kaitiaki-local-api."""

from typing import Any

from pydantic import BaseModel, Field


class IntakeRequest(BaseModel):
    source_id: str = Field(..., min_length=1)
    target_pou: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    metadata: dict[str, Any] = Field(default_factory=dict)
    tapu_level: str = "caution"


class IntakeResponse(BaseModel):
    intake_id: str
    target_pou: str
    allowed: bool
    cleaned: bool
    meta_scrubbed: bool
    ready_for_indexing: bool
    promoted: bool
    stage_db: str
    endpoint_db: str | None = None


class SearchResult(BaseModel):
    target_pou: str
    intake_id: str
    chunk_id: str
    chunk_index: int
    chunk_text: str
    source_id: str
    score: int


class SemanticChunkCandidate(BaseModel):
    target_pou: str
    intake_id: str
    chunk_id: str
    chunk_index: int
    source_id: str
    embedding_input: str


class SemanticIndexResult(BaseModel):
    indexed_chunks: int
    embedding_model: str
    embedding_mode: str
    by_pou: dict[str, int]
