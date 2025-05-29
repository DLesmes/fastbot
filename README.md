# FastBot

FastBot is a powerful AI chatbot built with FastAPI and Google's Gemini model, featuring advanced document retrieval and conversation memory capabilities.

## Overview

FastBot is designed to provide intelligent responses by combining:
- Real-time conversation memory
- Document retrieval and context awareness
- Configurable prompt templates
- Version-based model configurations

## Features

- 🤖 **Advanced LLM Integration**: Powered by Google's Gemini model
- 📚 **Document Retrieval**: Intelligent document search and context integration
- 💾 **Conversation Memory**: Maintains context across conversations
- ⚙️ **Configurable Templates**: Version-based prompt templates
- 🔄 **State Management**: Persistent conversation state
- 📝 **Document Processing**: PDF processing and vector storage
- 🔍 **Semantic Search**: Advanced document retrieval using embeddings

## Data Formats

### Message Format
```json
{
    "session_id": "string",
    "message": "string",
    "timestamp": "integer",
    "role": "string"
}
```

### Response Format
```json
{
    "status": "success|error",
    "session_id": "string",
    "message": "string",
    "response": "string",
    "timestamp": "integer",
    "role": "string",
    "context": "string"
}
```

## Prerequisites

- Python 3.8+
- Google API Key for Gemini
- UV package manager

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastbot.git
cd fastbot
```

2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```
### Configuration

#### Environment Variables
```env
APP_NAME=FastBot
DEBUG=True
LLM_VERSION=v1
GOOGLE_API_KEY=your_api_key_here
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

4. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Chat Endpoint
```bash
POST /api/v1/chat
```

Query Parameters:
- `session_id`: Unique identifier for the conversation
- `message`: User's message
- `role`: Message role (default: "user")



### Prompt Templates
Templates are configured in `config/prompts.yml` with version-specific settings.

## Project Structure
fastbot/
├── config/
│ └── prompts.yml
├── models/
│ ├── message.py
│ └── state.py
├── services/
│ ├── agent.py
│ ├── memory.py
│ └── retriever.py
├── controllers/
│ └── chat.py
├── clients/
│ └── llm/
│ └── gemini_client.py
├── main.py
├── settings.py
└── requirements.txt

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Use meaningful commit messages

## Contact

- Project Link: [https://github.com/dlesmes/fastbot](https://github.com/dlesmes/fastbot)
- Email: your.email@example.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini](https://ai.google.dev/)
- [LangChain](https://python.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)

