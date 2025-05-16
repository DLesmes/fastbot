from clients.llm.gemini_client import GeminiClient
from models.message import Message
from services.memory import memory
from services.retriever import retriever
from settings import settings
from typing import Dict, Any

class Agent:
    def __init__(self):
        self.llm_client = GeminiClient()
        self.memory = memory
    
    async def process_message(self, message: Message) -> Dict[str, Any]:
        try:
            # Get conversation history
            state = self.memory.get_state(message.session_id)
            conversation_context = state.get_context()
            
            # Get relevant documents
            retrieved_docs = retriever.get_relevant_documents(message.message)
            docs_text = "\n".join([doc.page_content for doc in retrieved_docs])
            
            # Use docs template from settings directly
            full_message = settings.docs.format(
                context=conversation_context,
                docs_text=docs_text,
                message=message.message
            )
            
            # Update state with the full message
            state.update_context(full_message)
            
            # Get response from LLM
            response = await self.llm_client.get_response(full_message)
            
            # Create message objects
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
            
            # Update memory
            self.memory.update_state(message.session_id, user_message)
            self.memory.update_state(message.session_id, assistant_message)
            
            return {
                "status": "success",
                "session_id": message.session_id,
                "message": message.message,
                "response": response["content"],
                "timestamp": message.timestamp,
                "role": message.role,
                "context": full_message
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
