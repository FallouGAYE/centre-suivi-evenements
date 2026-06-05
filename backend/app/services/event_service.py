from collections import Counter
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


def get_user_summary(db: Session, user_id: str):
    events = (
        db.query(Event)
        .filter(Event.user_id == user_id)
        .order_by(Event.created_at.asc())
        .all()
    )

    if not events:
        return {
            "user_id": user_id,
            "total_events": 0,
            "event_types": {},
            "first_event": None,
            "last_event": None,
        }

    event_types = Counter(event.type for event in events)

    return {
        "user_id": user_id,
        "total_events": len(events),
        "event_types": dict(event_types),
        "first_event": events[0].created_at,
        "last_event": events[-1].created_at,
    }