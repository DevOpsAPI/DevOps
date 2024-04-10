from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import Optional

app = FastAPI()
default_message = "Hallo!"
models.Base.metadata.create_all(bind=engine)

class Genre(BaseModel):
    genre_id: int
    genre_name: str

class Game_Publisher(BaseModel):
    game_publisher_id: int
    game_publisher_name: str

class Game(BaseModel):
    title: str
    genres: Optional[Genre] = None
    game_publishers: Optional[Game_Publisher] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return default_message

@app.post("/genre/")
def create_genre(genre: Genre, db: Session = Depends(get_db)):
    db_genre = models.Genre(genre_name=genre.genre_name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre
