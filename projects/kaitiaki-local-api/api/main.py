"""Minimal FastAPI surface for the first local Kaitiaki API project."""

from fastapi import FastAPI

from app.settings import settings
from services.guardian import route_guardian_action
from services.inference import inference_profile

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
