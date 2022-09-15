from sqlite3 import Date
from pydantic import BaseModel
from datetime import date, datetime

class Post(BaseModel):
    id: str
    title: str
    body: str
    votes: int
    date: datetime

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class PostVote(BaseModel):
    id: str
