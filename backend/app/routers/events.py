from fastapi import APIRouter
from app.schemas.event import EventCreate
from app.services.event_service import add_event, get_all_events

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("")
def create_event(event: EventCreate):

    add_event(event.dict())

    return {
        "message": "Event created"
    }

@router.get("")
def get_events():
    return get_all_events()