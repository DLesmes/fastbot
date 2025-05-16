from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class State(BaseModel):
    session_id: str
    messages: List[Dict[str, Any]] = []
    context: str = ""
    last_updated: int = int(datetime.now().timestamp())
    
    def add_message(self, message: Dict[str, Any]) -> None:
        self.messages.append(message)
        if len(self.messages) > 10:  # Keep only last 10 messages
            self.messages.pop(0)
        self.last_updated = int(datetime.now().timestamp())
    
    def get_context(self) -> str:
        return "\n".join([
            f"{msg['role']}: {msg['message']}"
            for msg in self.messages[-10:]  # Get last 10 messages
        ])
    
    def update_context(self, new_context: str) -> None:
        self.context = new_context
