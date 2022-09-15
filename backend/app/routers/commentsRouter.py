from wsgiref.util import setup_testing_defaults
from ..schemas import commentSchema

from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from ..repositories.database import SessionLocal
from .. repositories import commentCrud


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={404: {"description": "Not found"}}
)


@router.get('/{post_id}', response_model=list[commentSchema.Comment])
async def comment(post_id: str, skip: int = 0, limit: int = 20,
 db: Session = Depends(get_db)):
    comments = commentCrud.get_comments_by_post_id(db, post_id, skip, limit)
    return comments


@router.post("/create_comment", response_model=commentSchema.Comment)
async def create_comment(userComment: commentSchema.CommentCreate, db: Session = Depends(get_db)):
    db_comment = commentCrud.create_comment(db, userComment.body, userComment.post_id)
    return db_comment


@router.post("/upvote", response_model=commentSchema.Comment)
async def upvote(comment_id: str, db: Session = Depends(get_db)):
    print("Trying to upvote...")
    print("Comment id: ", comment_id)
    comment = commentCrud.upvote(db, comment_id)    
    return comment


@router.post("/downvote", response_model=commentSchema.Comment)
async def downvote(comment_id: str, db: Session = Depends(get_db)):
    comment = commentCrud.downvote(db, comment_id)    
    return comment
