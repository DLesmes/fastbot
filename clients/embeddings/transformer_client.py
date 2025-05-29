from langchain_huggingface import HuggingFaceEmbeddings
from settings import settings

class TransformerClient:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.embedding_model
        )
    
    def get_embeddings(self):
        return self.embeddings

# Create a single instance
transformer_client = TransformerClient()
