from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    session_id: str
    message: str
    timestamp: int = int(datetime.now().timestamp())
    role: str = "user"
