import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Base

username = 'doadmin'
host = 'db-mysql-nyc3-46112-do-user-16006876-0.c.db.ondigitalocean.com'
port = 25060
database = 'defaultdb'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import games

    Base.metadata.create_all(bind=engine)