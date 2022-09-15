from sqlalchemy import Integer, String, Column, VARCHAR
from sqlalchemy.orm import relationship
from ..repositories.database import Base
from uuid import uuid4

def get_uuid():
    return uuid4().hex

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column(VARCHAR, primary_key=True, unique = True,index=True, default=get_uuid())
    post_id = Column(VARCHAR, primary_key=True, unique = True,index=True, default=get_uuid())
    body = Column(VARCHAR)
    votes = Column(Integer)

    