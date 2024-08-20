from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome to my world": "Hello World"}

def test_get_posts():
    payload = {"key": "value"}
    response = client.post("/posts", json=payload) 
    assert response.status_code == 200
    assert response.json() == {"posts": "This is a post"}
    