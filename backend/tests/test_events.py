from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_event():
    response = client.post(
        "/events",
        json={
            "user_id": "test_user",
            "type": "login",
            "payload": {"ip": "127.0.0.1"}
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Event created"
    assert "id" in response.json()


def test_get_events():
    response = client.get("/events")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_user_summary():
    response = client.get("/users/test_user/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["user_id"] == "test_user"
    assert "total_events" in data
    assert "event_types" in data