"""Minimal guardian stub for the first local API carve."""

from typing import Iterable

ALLOWED_POU = {"whakapapa", "tikanga", "taonga", "rongo", "whakairo", "tapu"}


def route_guardian_action(target_pou: str, visible_pou: Iterable[str] | None = None) -> bool:
    """Return True only when the requested pou is within the visible local scope."""
    scope = set(visible_pou or ALLOWED_POU)
    return target_pou in scope


def guardian_intake_decision(target_pou: str, tapu_level: str) -> dict[str, object]:
    """Return the local-first guardian decision for an intake request."""
    allowed = route_guardian_action(target_pou)
    return {
        "target_pou": target_pou,
        "tapu_level": tapu_level,
        "allowed": allowed,
        "reason": "allowed_local_scope" if allowed else "blocked_unknown_pou",
    }
