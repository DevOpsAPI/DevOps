from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PASSWORD")
db_host = os.environ.get("MYSQL_HOST")
db_port = os.environ.get("MYSQL_PORT")
db_name = os.environ.get("MYSQL_DB")

if db_user is None or db_password is None or db_host is None or db_port is None or db_name is None:
    print(db_user, db_password, db_host, db_port, db_name)
    raise Exception("Please set the environment variables MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT and MYSQL_DB")
else:  
    URL_DATABASE = f'mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()