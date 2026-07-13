import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi.testclient import TestClient

from app.server import app

client = TestClient(app)


def test_analyze_campaign():

    response = client.post(
        "/api/v1/analyze",
        json={
            "campaign_id": "CMP-101",
            "question": "Why are conversions low?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "campaign" in data
    assert "metrics" in data
    assert "orders" in data
    assert "conflicts" in data