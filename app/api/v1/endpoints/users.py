from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.dependencies.deps import get_db

router = APIRouter()


@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()
