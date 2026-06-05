from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.event_service import get_user_summary

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}/summary")
def summary(
    user_id: str,
    db: Session = Depends(get_db)
):
    return get_user_summary(db, user_id)