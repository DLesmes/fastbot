from pydantic_settings import BaseSettings
from pathlib import Path
import yaml
from typing import Dict, Any

class Settings(BaseSettings):
    app_name: str = "FastBot"
    debug: bool = True
    llm_version: str = "v1"
    google_api_key: str = ""
    model_name: str = "gemini-2.0-flash-lite"
    system_prompt: str = ""
    temperature: float = 0.7
    max_tokens: int = 2000
    parameters: Dict[str, Any] = {}
    docs: str
    chunk_size: int = 1000
    chunk_overlap: int = 200
    embedding_model: str = "all-MiniLM-L6-v2"
    
    def __init__(self, **kwargs):
        # Load version-specific configuration first
        config_path = Path(__file__).parent / "config" / "prompts.yml"
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            version_config = config['versions'].get(kwargs.get('llm_version', 'v1'), {})
            # Update kwargs with version-specific values
            kwargs.update(version_config)
        
        super().__init__(**kwargs)

    class Config:
        env_file = ".env"

settings = Settings()