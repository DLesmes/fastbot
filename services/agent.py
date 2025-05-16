from clients.llm.gemini_client import GeminiClient
from models.message import Message
from services.memory import memory  # Import the memory instance directly
from typing import Dict, Any

class Agent:
    def __init__(self):
        self.llm_client = GeminiClient()
        self.memory = memory  # Use the imported memory instance
    
    async def process_message(self, message: Message) -> Dict[str, Any]:
        try:
            # Get conversation history
            state = self.memory.get_state(message.session_id)
            context = state.get_context()
            
            # Prepare message with context
            full_message = f"Previous conversation:\n{context}\n\nCurrent message: {message.message}"
            
            # Get response from LLM
            response = await self.llm_client.get_response(full_message)
            
            # Create message objects for both user and assistant
            user_message = {
                "message": message.message,
                "timestamp": message.timestamp,
                "role": message.role
            }
            
            assistant_message = {
                "message": response["content"],
                "timestamp": message.timestamp,
                "role": "assistant"
            }
            
            # Update memory with both messages
            self.memory.update_state(message.session_id, user_message)
            self.memory.update_state(message.session_id, assistant_message)
            
            return {
                "status": "success",
                "session_id": message.session_id,
                "message": message.message,
                "response": response["content"],
                "timestamp": message.timestamp,
                "role": message.role,
                "context": context
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
