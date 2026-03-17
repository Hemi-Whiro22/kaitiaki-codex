"""Local project settings for the first Kaitiaki API carve."""

import os
from pathlib import Path

from pydantic import BaseModel


class ProjectSettings(BaseModel):
    project_name: str = "kaitiaki-local-api"
    project_root: Path = Path(__file__).resolve().parents[1]
    api_host: str = os.getenv("KAITIAKI_API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("KAITIAKI_API_PORT", "8093"))
    mcp_host: str = os.getenv("KAITIAKI_MCP_HOST", "0.0.0.0")
    mcp_port: int = int(os.getenv("KAITIAKI_MCP_PORT", "8172"))
    mcp_transport: str = os.getenv("KAITIAKI_MCP_TRANSPORT", "streamable-http")
    mcp_path: str = os.getenv("KAITIAKI_MCP_PATH", "/mcp")
    inference_endpoint: str = os.getenv("KAITIAKI_INFERENCE_ENDPOINT", "http://127.0.0.1:8090")
    embedding_mode: str = os.getenv("KAITIAKI_EMBED_MODE", "light-v2-fallback")
    embedding_model: str = os.getenv("KAITIAKI_EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    embedding_dim: int = int(os.getenv("KAITIAKI_EMBED_DIM", "64"))
    local_first: bool = True


settings = ProjectSettings()
