from pydantic_settings import BaseSettings
from pathlib import Path
import yaml
from typing import Dict, Any

class Settings(BaseSettings):
    app_name: str = "FastBot"
    debug: bool = True
    llm_version: str = "v1"
    google_api_key: str = ""
    model_name: str = "gemini-1.5-flash-lite"
    system_prompt: str = ""
    temperature: float = 0.7
    max_tokens: int = 2000
    parameters: Dict[str, Any] = {}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load version-specific configuration
        config_path = Path(__file__).parent / "config" / "prompts.yml"
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                version_config = config['versions'].get(self.llm_version, {})
                
                # Update settings with version-specific values
                self.model_name = version_config.get('model_name', self.model_name)
                self.system_prompt = version_config.get('system_prompt', self.system_prompt)
                self.temperature = version_config.get('temperature', self.temperature)
                self.max_tokens = version_config.get('max_tokens', self.max_tokens)
                self.parameters = version_config.get('parameters', self.parameters)
        except Exception as e:
            print(f"Error loading prompt config: {e}")

    class Config:
        env_file = ".env"

settings = Settings()
