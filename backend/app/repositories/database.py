from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.config import *

print("Host: ", DATABASE_HOST)

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_KEY}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()