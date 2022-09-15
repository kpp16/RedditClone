from xml.etree.ElementTree import Comment
from sqlalchemy.orm import Session

from ..models.comment import Comment
from ..schemas import commentSchema
from uuid import uuid4

def get_uuid():
    return uuid4().hex


def create_comment(db: Session, body: str, post_id: str):
    comment_id = get_uuid()
    db_comment = Comment(comment_id = comment_id, post_id = post_id, body = body, votes = 0)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: str):
    db_comment = db.query(Comment).filter(comment_id == comment_id).first()
    return db_comment


def get_comments_by_post_id(db: Session, post_id: str, skip: int = 0, limit: int = 20):
    comments = db.query(Comment).filter(post_id == post_id).offset(skip).limit(limit).all()
    return comments


def upvote(db: Session, comment_id: str):
    print("Inside upvote comment")
    comment = get_comment(db, comment_id)
    votes = comment.votes
    print("prev votes: ", votes)
    votes += 1
    db.query(Comment).filter(comment_id == comment_id).update({"votes": votes})
    db.commit()
    return get_comment(db, comment_id)


def downvote(db: Session, comment_id: str):
    comment = get_comment(db, comment_id)
    votes = comment.votes
    votes -= 1
    db.query(Comment).filter(comment_id == comment_id).update({"votes": votes})
    db.commit()
    return get_comment(db, comment_id)   