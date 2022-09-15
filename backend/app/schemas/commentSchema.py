from pydantic import BaseModel

class Comment(BaseModel):
    post_id: str
    comment_id: str
    body: str
    votes: int

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    body: str
    post_id: str

    class Config:
        orm_mode = True

class CommentVote(BaseModel):
    comment_id: str