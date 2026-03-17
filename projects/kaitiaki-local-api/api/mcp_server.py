"""Minimal FastMCP surface for the first local Kaitiaki API project."""

from mcp.server.fastmcp import FastMCP

from app.models import IntakeRequest
from app.settings import settings
from services.guardian import route_guardian_action
from services.inference import inference_profile
from services.extract import scan_archive_folder
from services.intake import (
    ingest_archive_folder,
    ingest_intake,
    intake_summary,
    search_intake,
    semantic_ready_chunks,
)
from services.vector_index import semantic_search, sync_semantic_index

mcp = FastMCP(
    settings.project_name,
    host=settings.mcp_host,
    port=settings.mcp_port,
    streamable_http_path=settings.mcp_path,
)


@mcp.tool
def guardian_check(target_pou: str) -> bool:
    """Return whether the requested pou is currently allowed in local scope."""
    return route_guardian_action(target_pou)


@mcp.tool
def inference_info() -> dict[str, object]:
    """Expose the local inference configuration for this project."""
    return inference_profile()


@mcp.tool
def intake_text(source_id: str, target_pou: str, content: str, is_tapu: bool = False) -> dict[str, object]:
    """Run a local-first intake through guardian, scrub, staging, and promotion."""
    result = ingest_intake(
        IntakeRequest(
            source_id=source_id,
            target_pou=target_pou,
            content=content,
            is_tapu=is_tapu,
        )
    )
    return result.__dict__


@mcp.tool
def archive_scan(folder_path: str) -> dict[str, object]:
    """Inspect a local archive folder and classify text-bearing files and assets."""
    return scan_archive_folder(folder_path)


@mcp.tool
def archive_ingest(folder_path: str, target_pou: str, is_tapu: bool = False, max_text_files: int = 50) -> dict[str, object]:
    """Ingest a local archive folder, promoting text-bearing records and registering assets."""
    return ingest_archive_folder(
        folder_path=folder_path,
        target_pou=target_pou,
        is_tapu=is_tapu,
        max_text_files=max_text_files,
    ).__dict__


@mcp.tool
def search_intake_chunks(query: str, target_pou: str | None = None, limit: int = 5) -> list[dict[str, object]]:
    """Search promoted local intake chunks by simple text match."""
    return [result.model_dump() for result in search_intake(query, target_pou=target_pou, limit=limit)]


@mcp.tool
def intake_overview() -> dict[str, object]:
    """Expose local intake staging and endpoint counts."""
    return intake_summary()


@mcp.tool
def semantic_ready_overview(target_pou: str | None = None, limit: int = 20) -> list[dict[str, object]]:
    """Expose chunks ready for future semantic/vector indexing."""
    return [result.model_dump() for result in semantic_ready_chunks(target_pou=target_pou, limit=limit)]


@mcp.tool
def semantic_index_sync(target_pou: str | None = None, limit: int = 100) -> dict[str, object]:
    """Build or refresh the local semantic index from promoted chunks."""
    return sync_semantic_index(target_pou=target_pou, limit=limit)


@mcp.tool
def semantic_search_chunks(query: str, target_pou: str | None = None, limit: int = 5) -> list[dict[str, object]]:
    """Search the local semantic index using the current embedding profile."""
    return [result.model_dump() for result in semantic_search(query, target_pou=target_pou, limit=limit)]


app = mcp.streamable_http_app()


if __name__ == "__main__":
    mcp.run(transport=settings.mcp_transport)
