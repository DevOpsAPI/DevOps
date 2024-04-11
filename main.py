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

@app.post("/game_publisher/")
def create_game_publisher(game_publisher: Game_Publisher, db: Session = Depends(get_db)):
    db_game_publisher = models.Game_Publisher(game_publisher_name=game_publisher.game_publisher_name)
    db.add(db_game_publisher)
    db.commit()
    db.refresh(db_game_publisher)
    return db_game_publisher

@app.delete("/genre/{genre_id}")
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.genre_id == genre_id).first()
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(db_genre)
    db.commit()
    return db_genre