"""Shared request and response models for kaitiaki-local-api."""

from typing import Any

from pydantic import BaseModel, Field


class IntakeRequest(BaseModel):
    source_id: str = Field(..., min_length=1)
    target_pou: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    metadata: dict[str, Any] = Field(default_factory=dict)
    is_tapu: bool = False


class ArchiveFolderRequest(BaseModel):
    folder_path: str = Field(..., min_length=1)
    target_pou: str = Field(..., min_length=1)
    is_tapu: bool = False
    max_text_files: int = Field(default=50, ge=1, le=500)


class IntakeResponse(BaseModel):
    intake_id: str
    target_pou: str
    allowed: bool
    is_tapu: bool
    resolved_tapu_level: str | None = None
    reason: str
    confirmation_required: bool = False
    required_tapu_level: str | None = None
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


class ArchiveScanResponse(BaseModel):
    folder_path: str
    archive_kind: str
    file_counts: dict[str, int]
    text_candidates: list[str]
    asset_candidates: list[str]


class ArchiveIngestResponse(BaseModel):
    archive_id: str
    folder_path: str
    target_pou: str
    is_tapu: bool
    resolved_tapu_level: str | None
    ingested_text_files: int
    registered_assets: int
    blocked: bool
    reason: str
