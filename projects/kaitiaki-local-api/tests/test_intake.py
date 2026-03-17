from pathlib import Path

from fastapi.testclient import TestClient

from api.main import app
from app.settings import settings


client = TestClient(app)


def test_intake_promotes_to_target_db() -> None:
    response = client.post(
        "/intake",
        json={
            "source_id": "sample-source",
            "target_pou": "tikanga",
            "content": "Kia ora  \n\nThis is a local intake record.\u00a0",
            "metadata": {
                "title": "Sample intake",
                "author_email": "private@example.com",
                "tags": ["sample"],
            },
            "is_tapu": False,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is True
    assert data["is_tapu"] is False
    assert data["resolved_tapu_level"] == "open"
    assert data["promoted"] is True
    assert Path(data["stage_db"]).exists()
    assert Path(data["endpoint_db"]).exists()
    assert data["reason"] == "allowed_local_scope"

    fetch = client.get(f"/intake/{data['intake_id']}")
    assert fetch.status_code == 200
    staged = fetch.json()
    assert staged["promoted"] == 1
    assert staged["metadata_json"]["meta_scrub_note"] == "sensitive metadata removed"
    assert "private@example.com" not in str(staged["metadata_json"])


def test_search_finds_promoted_chunk() -> None:
    response = client.post(
        "/intake",
        json={
            "source_id": "search-source",
            "target_pou": "whakapapa",
            "content": "Whakapapa memory grows through local intake and recall.",
            "metadata": {"title": "Search sample"},
            "is_tapu": False,
        },
    )
    assert response.status_code == 200

    search = client.get("/search", params={"q": "recall", "target_pou": "whakapapa"})
    assert search.status_code == 200
    results = search.json()
    assert results
    assert any(item["target_pou"] == "whakapapa" for item in results)


def test_intake_blocks_low_tapu_for_target_lane() -> None:
    response = client.post(
        "/intake",
        json={
            "source_id": "blocked-source",
            "target_pou": "tapu",
            "content": "This should not be promoted with open tapu level.",
            "metadata": {"title": "Blocked sample"},
            "is_tapu": False,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is False
    assert data["promoted"] is False
    assert data["reason"] == "blocked_noa_for_tapu_lane"
    assert data["confirmation_required"] is True
    assert data["required_tapu_level"] == "restricted"
    assert data["is_tapu"] is False
    assert data["resolved_tapu_level"] == "open"
    assert data["intake_id"] == "blocked"
    assert data["endpoint_db"] is None


def test_intake_overview_reports_counts() -> None:
    overview = client.get("/intake")
    assert overview.status_code == 200
    data = overview.json()
    assert "staged_records" in data
    assert "endpoint_counts" in data


def test_file_intake_html_normalizes_to_text() -> None:
    response = client.post(
        "/intake/file",
        data={
            "source_id": "html-source",
            "target_pou": "taonga",
            "metadata_json": "{\"title\": \"HTML sample\"}",
            "is_tapu": "false",
        },
        files={
            "file": ("sample.html", b"<html><body><h1>Kia ora</h1><p>Semantic recall text</p></body></html>", "text/html")
        },
    )
    assert response.status_code == 200
    data = response.json()
    fetch = client.get(f"/intake/{data['intake_id']}")
    assert fetch.status_code == 200
    staged = fetch.json()
    assert "Kia ora" in staged["content_clean"]
    assert "Semantic recall text" in staged["content_clean"]


def test_semantic_ready_returns_candidates() -> None:
    response = client.get("/semantic-ready")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("embedding_input" in item for item in data)


def test_semantic_index_and_search_work() -> None:
    seed = client.post(
        "/intake",
        json={
            "source_id": "semantic-source",
            "target_pou": "tikanga",
            "content": "Light v2 style semantic indexing should recall tikanga context.",
            "metadata": {"title": "Semantic seed"},
            "is_tapu": False,
        },
    )
    assert seed.status_code == 200

    sync = client.post("/index/semantic-sync")
    assert sync.status_code == 200
    sync_data = sync.json()
    assert sync_data["indexed_chunks"] >= 1

    search = client.get("/search/semantic", params={"q": "tikanga context"})
    assert search.status_code == 200
    results = search.json()
    assert results
    assert any(item["target_pou"] == "tikanga" for item in results)
