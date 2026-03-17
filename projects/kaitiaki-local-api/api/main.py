"""Minimal FastAPI surface for the first local Kaitiaki API project."""

import json

from fastapi import FastAPI, File, Form, HTTPException, Query, UploadFile

from app.models import (
    IntakeRequest,
    IntakeResponse,
    SearchResult,
    SemanticChunkCandidate,
    SemanticIndexResult,
)
from app.settings import settings
from services.extract import detect_source_type, extract_text_content
from services.guardian import route_guardian_action
from services.inference import inference_profile
from services.intake import (
    fetch_staged_intake,
    ingest_intake,
    intake_summary,
    search_intake,
    semantic_ready_chunks,
)
from services.vector_index import semantic_search, sync_semantic_index

app = FastAPI(title=settings.project_name)


@app.get("/health")
def health() -> dict[str, object]:
    return {"ok": True, "project": settings.project_name, "local_first": settings.local_first}


@app.get("/profile")
def profile() -> dict[str, object]:
    return {
        "api_port": settings.api_port,
        "mcp_port": settings.mcp_port,
        "inference": inference_profile(),
    }


@app.get("/guardian/{target_pou}")
def guardian_check(target_pou: str) -> dict[str, object]:
    return {"target_pou": target_pou, "allowed": route_guardian_action(target_pou)}


@app.post("/intake", response_model=IntakeResponse)
def intake(request: IntakeRequest) -> IntakeResponse:
    result = ingest_intake(request)
    return IntakeResponse(**result.__dict__)


@app.post("/intake/file", response_model=IntakeResponse)
async def intake_file(
    source_id: str = Form(...),
    target_pou: str = Form(...),
    is_tapu: bool = Form(False),
    metadata_json: str = Form("{}"),
    file: UploadFile = File(...),
) -> IntakeResponse:
    try:
        metadata = json.loads(metadata_json)
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=400, detail=f"invalid metadata_json: {exc}") from exc

    raw_bytes = await file.read()
    source_type = detect_source_type(file.filename, file.content_type)
    extracted_text = extract_text_content(raw_bytes, source_type)
    metadata = {
        **metadata,
        "filename": file.filename,
        "source_type": source_type,
        "content_type": file.content_type,
    }
    result = ingest_intake(
        IntakeRequest(
            source_id=source_id,
            target_pou=target_pou,
            content=extracted_text,
            metadata=metadata,
            is_tapu=is_tapu,
        )
    )
    return IntakeResponse(**result.__dict__)


@app.get("/intake/{intake_id}")
def intake_record(intake_id: str) -> dict[str, object]:
    record = fetch_staged_intake(intake_id)
    if record is None:
        raise HTTPException(status_code=404, detail="intake record not found")
    return record


@app.get("/intake")
def intake_overview() -> dict[str, object]:
    return intake_summary()


@app.get("/search", response_model=list[SearchResult])
def search(
    q: str = Query(..., min_length=1),
    target_pou: str | None = None,
    limit: int = Query(default=5, ge=1, le=20),
) -> list[SearchResult]:
    return search_intake(q, target_pou=target_pou, limit=limit)


@app.get("/search/semantic", response_model=list[SearchResult])
def search_semantic(
    q: str = Query(..., min_length=1),
    target_pou: str | None = None,
    limit: int = Query(default=5, ge=1, le=20),
) -> list[SearchResult]:
    return semantic_search(q, target_pou=target_pou, limit=limit)


@app.get("/semantic-ready", response_model=list[SemanticChunkCandidate])
def semantic_ready(
    target_pou: str | None = None,
    limit: int = Query(default=20, ge=1, le=100),
) -> list[SemanticChunkCandidate]:
    return semantic_ready_chunks(target_pou=target_pou, limit=limit)


@app.post("/index/semantic-sync", response_model=SemanticIndexResult)
def index_semantic_sync(
    target_pou: str | None = None,
    limit: int = Query(default=100, ge=1, le=500),
) -> SemanticIndexResult:
    result = sync_semantic_index(target_pou=target_pou, limit=limit)
    return SemanticIndexResult(**result)
