events_db = []

def add_event(event):
    events_db.append(event)

def get_all_events():
    return events_db

def filter_events(user_id=None, event_type=None):
    results = events_db

    if user_id:
        results = [
            e for e in results
            if e["user_id"] == user_id
        ]

    if event_type:
        results = [
            e for e in results
            if e["type"] == event_type
        ]

    return results