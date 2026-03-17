from services.guardian import route_guardian_action


def test_guardian_allows_known_pou() -> None:
    assert route_guardian_action("tikanga") is True


def test_guardian_blocks_unknown_pou() -> None:
    assert route_guardian_action("unknown") is False
