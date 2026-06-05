from fastapi import FastAPI
from app.routers import events

from app.database import engine
from app.models.event import Event

Event.metadata.create_all(bind=engine)

app = FastAPI(title="centre de suivi des événements")

app.include_router(events.router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }