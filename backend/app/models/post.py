from sqlalchemy import Integer, String, Column, VARCHAR, Date
from sqlalchemy.orm import relationship
from ..repositories.database import Base
from uuid import uuid4

def get_uuid():
    return uuid4().hex

class Post(Base):
    __tablename__ = "posts"

    id = Column(VARCHAR, primary_key=True, unique = True,index=True, default=get_uuid())   
    title = Column(VARCHAR)
    body = Column(VARCHAR)
    votes = Column(Integer)
    date = Column(Date)

    