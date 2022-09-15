from sqlalchemy.orm import Session
from sqlalchemy import desc

from app import models
from ..models.post import Post
from ..schemas import postSchema
from uuid import uuid4

from datetime import datetime


def get_uuid():
    return uuid4().hex


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).order_by(Post.date).offset(skip).limit(limit).all()


def get_post(db: Session, id: int):
    return db.query(Post).filter(Post.id == id).first()


def create_post(db: Session, post: postSchema.PostCreate):
    db_post = Post(title = post.title,
                   body = post.body,
                   id = get_uuid(),
                   votes = 0,
                   date = datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


def upvote_post(db: Session, id: int):
    post = get_post(db, id)
    votes = post.votes
    db.query(Post).filter(Post.id == id).update({'votes': votes+1})
    db.commit()
    return get_post(db, id)


def downvote_post(db: Session, id: int):
    post = get_post(db, id)
    votes = post.votes
    db.query(Post).filter(Post.id == id).update({'votes': votes-1})
    db.commit()
    return get_post(db, id)