from fastapi import APIRouter, HTTPException
from models.message import Message
from services.agent import Agent
from typing import Dict, Any

router = APIRouter()
agent = Agent()

@router.post("/chat")
async def chat(
    session_id: str,
    message: str,
    role: str = "user"
) -> Dict[str, Any]:
    try:
        # Create message object with query parameters
        message_obj = Message(
            session_id=session_id,
            message=message,
            role=role
        )
        
        response = await agent.process_message(message_obj)
        if response["status"] == "error":
            raise HTTPException(status_code=500, detail=response["error"])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
