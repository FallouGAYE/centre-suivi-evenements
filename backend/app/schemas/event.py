from pydantic import BaseModel
from typing import Optional, Dict, Any

class EventCreate(BaseModel):
    user_id: str
    type: str
    payload: Optional[Dict[str, Any]] = None