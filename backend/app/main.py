from fastapi import FastAPI
from app.routers import events

app = FastAPI(title="cente evenement API", version="1.0")

app.include_router(events.router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }