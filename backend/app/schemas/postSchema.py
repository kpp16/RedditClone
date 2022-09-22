from sqlite3 import Date
from pydantic import BaseModel

import datetime

class Post(BaseModel):
    id: str
    title: str
    body: str
    votes: int
    date: datetime.date

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class PostVote(BaseModel):
    id: str
