from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Game(BaseModel):
    game_id: int
    genre_id: int
    title: str

class Genre(BaseModel):
    genre_id: int
    genre_name: str

class Game_Publisher(BaseModel):
    game_publisher_id: int
    game_id: int
    publisher_id: int

class Publisher(BaseModel):
    publisher_id: int
    publisher_name: str

class Game_Platform(BaseModel):
    game_platform_id: int
    game_publisher_id: int
    platform_id: int
    release_date: str

class Platform(BaseModel):
    platform_id: int
    platform_name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/games/", status_code=status.HTTP_201_CREATED)
async def create_game(game: Game, db: Session = Depends(get_db)):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
