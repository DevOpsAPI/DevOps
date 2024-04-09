from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from database import Base

class Genre(Base):
    __tablename__ = "genres"
    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String(255), nullable=False, unique=True)

class Game_Publisher(Base):
    __tablename__ = "game_publishers"
    game_publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    game_publisher_name = Column(String(255), nullable=False, unique=True)

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey("genres.genre_id"))
    game_publisher_id = Column(Integer, ForeignKey("game_publishers.game_publisher_id"))
    title = Column(String(255), nullable=False, unique=True)

    genres = relationship("Genre")
    game_publishers = relationship("Game_Publisher")



   