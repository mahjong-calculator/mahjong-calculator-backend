import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(autouse=True, scope="session")
def mock_client():
    with TestClient(app) as client:
        yield client
