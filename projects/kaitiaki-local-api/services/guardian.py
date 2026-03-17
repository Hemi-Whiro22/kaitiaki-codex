"""Guardian routing and tapu enforcement for local intake."""

from typing import Iterable

ALLOWED_POU = {"whakapapa", "tikanga", "taonga", "rongo", "whakairo", "tapu"}
VALID_TAPU_LEVELS = ("open", "caution", "restricted", "sacred")
TAPU_ORDER = {level: index for index, level in enumerate(VALID_TAPU_LEVELS)}
MINIMUM_TAPU_BY_POU = {
    "whakairo": "open",
    "whakapapa": "open",
    "tikanga": "open",
    "rongo": "open",
    "taonga": "open",
    "tapu": "restricted",
}
NOA_LEVEL = "open"
TAPU_LEVEL = "restricted"


def route_guardian_action(target_pou: str, visible_pou: Iterable[str] | None = None) -> bool:
    """Return True only when the requested pou is within the visible local scope."""
    scope = set(visible_pou or ALLOWED_POU)
    return target_pou in scope


def guardian_intake_decision(target_pou: str, is_tapu: bool) -> dict[str, object]:
    """Return the local-first guardian decision for an intake request."""
    if not route_guardian_action(target_pou):
        return {
            "target_pou": target_pou,
            "is_tapu": is_tapu,
            "tapu_level": None,
            "allowed": False,
            "reason": "blocked_unknown_pou",
            "confirmation_required": False,
            "required_tapu_level": None,
        }

    minimum_tapu_level = MINIMUM_TAPU_BY_POU[target_pou]
    requested_tapu_level = TAPU_LEVEL if is_tapu else NOA_LEVEL
    if TAPU_ORDER[requested_tapu_level] < TAPU_ORDER[minimum_tapu_level]:
        return {
            "target_pou": target_pou,
            "is_tapu": is_tapu,
            "tapu_level": requested_tapu_level,
            "allowed": False,
            "reason": "blocked_noa_for_tapu_lane",
            "confirmation_required": True,
            "required_tapu_level": minimum_tapu_level,
        }

    return {
        "target_pou": target_pou,
        "is_tapu": is_tapu,
        "tapu_level": requested_tapu_level,
        "allowed": True,
        "reason": "allowed_local_scope",
        "confirmation_required": False,
        "required_tapu_level": minimum_tapu_level,
    }
