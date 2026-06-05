from fastapi import APIRouter
from app.schemas.event import EventCreate
from app.services.event_service import (
    add_event,
    filter_events
)

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("")
def create_event(event: EventCreate):

    add_event(event.model_dump())

    return {
        "message": "Event created"
    }

@router.get("")
def get_events(
    user_id: str | None = None,
    type: str | None = None
):
    return filter_events(
        user_id=user_id,
        event_type=type
    )