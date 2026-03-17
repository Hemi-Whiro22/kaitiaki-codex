"""Minimal FastMCP surface for the first local Kaitiaki API project."""

from mcp.server.fastmcp import FastMCP

from app.settings import settings
from services.guardian import route_guardian_action
from services.inference import inference_profile

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


app = mcp.streamable_http_app()


if __name__ == "__main__":
    mcp.run(transport=settings.mcp_transport)
