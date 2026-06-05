from fastapi import FastAPI

from app.database import engine
from app.models.event import Event
from app.routers import events, users

Event.metadata.create_all(bind=engine)

app = FastAPI(title="Piver Event Tracker API")

app.include_router(events.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }