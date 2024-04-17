#test_endpoints
from fastapi import FastAPI
from fastapi.testclient import TestClient
import logging
import pytest
from main import app, get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, StaticPool
from models import Base

 
client = TestClient(app)
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    database = TestingSessionLocal()
    Base.metadata.create_all(bind=engine)
    yield database
    database.close()


app.dependency_overrides[get_db] = override_get_db
 
def test_can_call_endpoint():
    response = client.get("/genre/")
    assert response.status_code == 200

genre_id = 1
genre_name = "TestingGenre"
game_publisher_id = 998
game_publisher_name = "TestingPublisher"

def test_create_genres():
    payload = {
    "genre_id": genre_id,
    "genre_name": genre_name
    }
    response = client.post("/genre/", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["genre_name"] == payload["genre_name"]

def test_create_game_publishers():
    payload = {
        "game_publisher_id": game_publisher_id,
        "game_publisher_name": game_publisher_name
    }
    response = client.post("/game_publisher/", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["game_publisher_name"] == payload["game_publisher_name"]

def test_create_games():
    payload = {
            "title": "TestGame",
            "genres": {
            "genre_id": genre_id,
            "genre_name": genre_name
            },
            "game_publishers": {
            "game_publisher_id": game_publisher_id,
            "game_publisher_name": game_publisher_name
            
            }
    }
    response = client.post("/games/", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == payload["title"]
    assert data["genres"]["genre_id"] == payload["genres"]["genre_id"]
    assert data["genres"]["genre_name"] == payload["genres"]["genre_name"]
    assert data["game_publishers"]["game_publisher_id"] == payload["game_publishers"]["game_publisher_id"]
    assert data["game_publishers"]["game_publisher_name"] == payload["game_publishers"]["game_publisher_name"]
    
 
def test_delete_game_publisher():
    response = client.delete(f"/game_publisher/{game_publisher_id}")
    assert response.status_code == 200
 
    data = response.json()
    print (data)