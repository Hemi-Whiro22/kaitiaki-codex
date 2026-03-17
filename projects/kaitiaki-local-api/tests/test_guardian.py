from services.guardian import guardian_intake_decision, route_guardian_action


def test_guardian_allows_known_pou() -> None:
    assert route_guardian_action("tikanga") is True


def test_guardian_blocks_unknown_pou() -> None:
    assert route_guardian_action("unknown") is False


def test_guardian_blocks_tapu_level_below_lane_minimum() -> None:
    decision = guardian_intake_decision("tapu", False)
    assert decision["allowed"] is False
    assert decision["confirmation_required"] is True
    assert decision["required_tapu_level"] == "restricted"
    assert decision["reason"] == "blocked_noa_for_tapu_lane"


def test_guardian_allows_valid_lane_tapu_combination() -> None:
    decision = guardian_intake_decision("tikanga", False)
    assert decision["allowed"] is True
    assert decision["confirmation_required"] is False
    assert decision["tapu_level"] == "open"


def test_guardian_allows_tapu_lane_when_tapu_enabled() -> None:
    decision = guardian_intake_decision("tapu", True)
    assert decision["allowed"] is True
    assert decision["confirmation_required"] is False
    assert decision["tapu_level"] == "restricted"
