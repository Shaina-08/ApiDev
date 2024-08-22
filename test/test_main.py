from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome to my world": "Hello World"}

def test_get_posts():
    payload = {
        "title": "My First Post",
        "content": "This is the content of my first post",
    }
    response = client.post("/posts", json=payload)
    assert response.status_code == 201

    response_data = response.json()["data"]
    assert response_data["title"] == payload["title"]
    assert response_data["content"] == payload["content"]
    assert "id" in response_data 
    assert isinstance(response_data["id"], int)
    assert response_data["published"] is False
    assert response_data["rating"] is None
