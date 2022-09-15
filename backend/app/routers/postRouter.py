from ..schemas import postSchema
from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from ..repositories.database import SessionLocal
from ..repositories import postCrud

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}}
)

@router.get("/", response_model=list[postSchema.Post])
async def posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = postCrud.get_posts(db, skip=skip, limit=limit)
    return posts


@router.get("/{post_id}", response_model=postSchema.Post)
async def post(post_id: int, db: Session = Depends(get_db)):
    db_post = postCrud.get_post(db, post_id)
    if (db_post is None):
        raise HTTPException(status_code=404, detail="Post Not Found")
    return db_post


@router.post("/create_post", response_model=postSchema.Post)
async def create_post(newPost: postSchema.PostCreate, db: Session = Depends(get_db)):
    db_post = postCrud.create_post(db, newPost)
    return db_post


@router.post("/upvote", response_model=postSchema.Post)
async def upvote_post(vote: postSchema.PostVote, db: Session = Depends(get_db)):
    id = vote.id
    db_post = postCrud.upvote_post(db, id)
    return db_post


@router.post("/downvote", response_model=postSchema.Post)
async def downvote_post(vote: postSchema.PostVote, db: Session = Depends(get_db)):
    id = vote.id
    db_post = postCrud.downvote_post(db, id)
    return db_post

