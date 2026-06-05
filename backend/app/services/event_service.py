from collections import Counter
from app.models.event import Event

def get_user_summary(db, user_id: str):

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
            "last_event": None
        }

    event_types = Counter(
        event.type
        for event in events
    )

    return {
        "user_id": user_id,
        "total_events": len(events),
        "event_types": dict(event_types),
        "first_event": events[0].created_at,
        "last_event": events[-1].created_at
    }