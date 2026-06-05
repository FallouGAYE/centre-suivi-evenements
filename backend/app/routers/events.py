from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.event import EventCreate
from app.services.event_service import add_event, filter_events

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    created_event = add_event(db, event.model_dump())

    return {
        "message": "Event created",
        "id": created_event.id
    }

@router.get("")
def get_events(
    user_id: str | None = None,
    type: str | None = None,
    db: Session = Depends(get_db)
):
    return filter_events(
        db=db,
        user_id=user_id,
        event_type=type
    )