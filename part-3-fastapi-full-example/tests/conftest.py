import pytest
from app.api.main import create_app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(create_app())
