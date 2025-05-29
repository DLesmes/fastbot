from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from clients.embeddings.transformer_client import transformer_client
from settings import settings
import requests
from pathlib import Path
import tempfile

class Retriever:
    def __init__(self):
        self.embeddings = transformer_client.get_embeddings()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        self.vectorstore = None
        self._initialize_vectorstore()
    
    def _initialize_vectorstore(self):
        # Create or load the vectorstore
        persist_directory = Path("data/vectorstore")
        persist_directory.mkdir(parents=True, exist_ok=True)
        
        if (persist_directory / "chroma.sqlite3").exists():
            self.vectorstore = Chroma(
                persist_directory=str(persist_directory),
                embedding_function=self.embeddings
            )
        else:
            self._create_vectorstore()
    
    def _create_vectorstore(self):
        # Download and process the PDF
        pdf_url = "https://arxiv.org/pdf/2501.12948"
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
            response = requests.get(pdf_url)
            temp_file.write(response.content)
            temp_file_path = temp_file.name
        
        # Load and split the PDF
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()
        texts = self.text_splitter.split_documents(documents)
        
        # Create and persist the vectorstore
        persist_directory = Path("data/vectorstore")
        self.vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            persist_directory=str(persist_directory)
        )
        self.vectorstore.persist()
    
    def get_relevant_documents(self, query: str, k: int = 3) -> list:
        if not self.vectorstore:
            return []
        return self.vectorstore.similarity_search(query, k=k)

# Create a single instance
retriever = Retriever()
