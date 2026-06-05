from sqlalchemy.orm import Session
from app.models.event import Event

def add_event(db: Session, event_data: dict):
    event = Event(**event_data)
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def filter_events(db: Session, user_id=None, event_type=None):
    query = db.query(Event)

    if user_id:
        query = query.filter(Event.user_id == user_id)

    if event_type:
        query = query.filter(Event.type == event_type)

    return query.order_by(Event.created_at.desc()).all()