from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, Any
from settings import settings

class GeminiClient:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=settings.model_name,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            google_api_key=settings.google_api_key,
            **settings.parameters
        )
    
    async def get_response(self, message: str) -> Dict[str, Any]:
        try:
            # Add system prompt to the message
            full_message = f"{settings.system_prompt}\n\n{message}"
            response = await self.model.ainvoke(full_message)
            return {
                "content": response.content,
                "status": "success"
            }
        except Exception as e:
            return {
                "content": str(e),
                "status": "error"
            }
