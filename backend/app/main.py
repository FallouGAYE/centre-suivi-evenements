from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.event import Event
from app.routers import events, users

Event.metadata.create_all(bind=engine)

app = FastAPI(title="centre de suivi d'événements", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(events.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }