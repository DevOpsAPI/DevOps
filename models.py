from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import sessionmaker, relationship
from database import Base

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_id = Column(Integer, ForeignKey("genres.genre_id"), nullable=False)
    title = Column(String(255))

    genre_name = relationship("Genre", back_populates="games")
    game_publisher = relationship("Game_Publisher", back_populates="games")

class Genre(Base):
    __tablename__ = "genres"
    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String(255))

    games = relationship("Game", back_populates="genre_name")

class Game_Publisher(Base):
    __tablename__ = "game_publishers"
    game_publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey("games.game_id"), nullable=False)
    publisher_id = Column(Integer, ForeignKey("publishers.publisher_id"), nullable=False)

    games = relationship("Game", back_populates="game_publisher")
    publishers = relationship("Publisher", back_populates="games")
    game_platforms = relationship("Game_Platform", back_populates="game_publisher")

class Publisher(Base):
    __tablename__ = "publishers"
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String(255))
    
    games = relationship("Game_Publisher", back_populates="publishers")


class Game_Platform(Base):
    __tablename__ = "game_platforms"
    game_platform_id = Column(Integer, primary_key=True, autoincrement=True)
    game_publisher_id = Column(Integer, ForeignKey("game_publishers.game_publisher_id"), nullable=False)
    platform_id = Column(Integer, ForeignKey("platforms.platform_id"), nullable=False)

    game_publisher = relationship("Game_Publisher", back_populates="game_platforms")
    platform_name = relationship("Platform", back_populates="game_platforms")

class Platform(Base):
    __tablename__ = "platforms"
    platform_id = Column(Integer, primary_key=True, autoincrement=True)
    platform_name = Column(String(255))

    game_platforms = relationship("Game_Platform", back_populates="platform_name")



   