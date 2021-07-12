from fastapi.testclient import TestClient
import catana.main

client = TestClient(catana.main.app)


def test_index_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"version": 1}
