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

@app.get("/genre/")
def read_genres(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    genres = db.query(models.Genre).offset(skip).limit(limit).all()
    return genres

@app.delete("/genre/{genre_id}")
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.genre_id == genre_id).first()
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(db_genre)
    db.commit()
    return db_genre

@app.post("/game_publisher/")
def create_game_publisher(game_publisher: Game_Publisher, db: Session = Depends(get_db)):
    db_game_publisher = models.Game_Publisher(game_publisher_name=game_publisher.game_publisher_name)
    db.add(db_game_publisher)
    db.commit()
    db.refresh(db_game_publisher)
    return db_game_publisher

@app.get("/game_publisher/")
def read_game_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    game_publishers = db.query(models.Game_Publisher).offset(skip).limit(limit).all()
    return game_publishers

@app.delete("/game_publisher/{game_publisher_id}")
def delete_game_publisher(game_publisher_id: int, db: Session = Depends(get_db)):
    db_game_publisher = db.query(models.Game_Publisher).filter(models.Game_Publisher.game_publisher_id == game_publisher_id).first()
    if db_game_publisher is None:
        raise HTTPException(status_code=404, detail="Game Publisher not found")
    db.delete(db_game_publisher)
    db.commit()
    return db_game_publisher

@app.post("/games/", response_model=Game)
def create_game(game: Game, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.genre_id == game.genres).first()
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")

    db_publisher = db.query(models.Game_Publisher).filter(models.Game_Publisher.game_publisher_id == game.game_publishers).first()
    if db_publisher is None:
        raise HTTPException(status_code=404, detail="Game Publisher not found")

    db_game = models.Game(title=game.title, genre=db_genre, game_publisher=db_publisher)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game



