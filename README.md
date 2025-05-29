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

### Example Conversation
Here's a sample conversation showing how the chatbot maintains context and provides age-appropriate responses:

```json
{
  "status": "success",
  "session_id": "zxcvb",
  "message": "can you explain me this for a 5 years old child?",
  "response": "Okay! Imagine DeepSeek-R1 is like a really smart toy robot. At first, it tries to solve a puzzle, but it might not get it right away. But, the robot is learning!\n\nSometimes, it has a special \"aha!\" moment, like when you suddenly understand how to build a tower with blocks! The robot starts to think a little longer and checks its work. It's like the robot is saying, \"Hmm, maybe I can try a different way!\" This helps the robot get better at solving puzzles and other tricky things. It's all thanks to learning!",
  "timestamp": 1748492960,
  "role": "user",
  "context": "Previous conversation:\nuser: hello!!\nassistant: Hello there! How can I assist you today? I'm ready to provide accurate and concise information based on the documents you've provided. Just let me know what you'd like to know!\nuser: what is the latest model deployed by deepseek company?\nassistant: The latest model discussed in the provided documents is DeepSeek-R1.\n\nRelevant documents:\nDeepSeek-R1-Zero learns to allocate more thinking time to a problem by reevaluating its initial\napproach. This behavior is not only a testament to the model's growing reasoning abilities\nbut also a captivating example of how reinforcement learning can lead to unexpected and\nsophisticated outcomes.\nThis moment is not only an \"aha moment\" for the model but also for the researchers\nobserving its behavior. It underscores the power and beauty of reinforcement learning: rather\nthan explicitly teaching the model on how to solve a problem, we simply provide it with the\nright incentives, and it autonomously develops advanced problem-solving strategies. The\n\"aha moment\" serves as a powerful reminder of the potential of RL to unlock new levels of\nintelligence in artificial systems, paving the way for more autonomous and adaptive models in\nthe future.\n8\nbehaviors as the test-time computation increases. Behaviors such as reflection—where the model\nrevisits and reevaluates its previous steps—and the exploration of alternative approaches to\nproblem-solving arise spontaneously. These behaviors are not explicitly programmed but instead\nemerge as a result of the model's interaction with the reinforcement learning environment. This\nspontaneous development significantly enhances DeepSeek-R1-Zero's reasoning capabilities,\nenabling it to tackle more challenging tasks with greater efficiency and accuracy.\nAha Moment of DeepSeek-R1-ZeroA particularly intriguing phenomenon observed during\nthe training of DeepSeek-R1-Zero is the occurrence of an \"aha moment\". This moment, as\nillustrated in Table 3, occurs in an intermediate version of the model. During this phase,\nDeepSeek-R1-Zero learns to allocate more thinking time to a problem by reevaluating its initial\napproach. This behavior is not only a testament to the model's growing reasoning abilities\na clear view of how the model evolves over time, particularly in terms of its ability to handle\ncomplex reasoning tasks.\nAs depicted in Figure 3, the thinking time of DeepSeek-R1-Zero shows consistent improve-\n7\n\nCurrent message: can you explain me this for a 5 years old child?\n"
}
```

This example demonstrates:
- Session management with a unique `session_id`
- Context preservation across multiple messages
- Age-appropriate response adaptation
- Integration of document context
- Timestamp tracking
- Role-based message handling

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
│   └── prompts.yml
├── models/
│   ├── message.py
│   └── state.py
├── services/
│   ├── agent.py
│   ├── memory.py
│   └── retriever.py
├── controllers/
│   └── chat.py
├── clients/
│   ├── llm/
│   │   └── gemini_client.py
│   └── embeddings/
│       └── huggingface_client.py
├── data/
│   └── documents/
├── main.py
├── settings.py
├── pyproject.toml
└── .env.example

## Dependencies

The project uses modern Python packaging with `pyproject.toml` for dependency management. Key dependencies include:

- FastAPI: Modern web framework for building APIs
- Google Generative AI: For Gemini model integration
- LangChain: Framework for LLM applications
- ChromaDB: Vector database for document storage
- HuggingFace Embeddings: For document vectorization
- PyYAML: For configuration management

## Configuration Files

### pyproject.toml
The project uses `pyproject.toml` for dependency management and project metadata. This modern approach provides better dependency resolution and project configuration.

### prompts.yml
Located in the `config` directory, this YAML file contains version-specific prompt templates and configurations for the chatbot's responses.

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

