from sqlalchemy import Column, Integer, String, Date
from base import Base

class Game(Base):
    __tablename__ = "games"
    game_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    release_date = Column(Date)
    developer = Column(String)
    platform = Column(String)

