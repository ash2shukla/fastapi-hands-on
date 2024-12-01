from fastapi.testclient import TestClient


def test_resource1_get(client: TestClient):
    response = client.get("/resource1")
    assert response.json() == "resource1 get"
