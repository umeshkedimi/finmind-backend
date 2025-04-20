from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends


def get_db() -> Session:
    """
    Dependency that provides a database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
