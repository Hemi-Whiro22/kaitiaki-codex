"""Local inference adapter configuration for the first API carve."""

from app.settings import settings


def inference_profile() -> dict[str, object]:
    return {
        "endpoint": settings.inference_endpoint,
        "mode": "local-first",
        "draft_only": True,
    }
