from pydantic import BaseSettings
from pathlib import Path
import yaml
from typing import Dict, Any

class Settings(BaseSettings):
    app_name: str = "FastBot"
    debug: bool = True
    llm_version: str = "v1"  # Default version
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.llm_config = self._load_llm_config()
    
    def _load_llm_config(self) -> Dict[str, Any]:
        config_path = Path(__file__).parent / "config" / "prompts.yml"
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                return config['versions'].get(self.llm_version, {})
        except Exception as e:
            print(f"Error loading LLM config: {e}")
            return {}
    
    @property
    def model_name(self) -> str:
        return self.llm_config.get('model_name', 'gpt-3.5-turbo')
    
    @property
    def system_prompt(self) -> str:
        return self.llm_config.get('system_prompt', '')
    
    @property
    def temperature(self) -> float:
        return self.llm_config.get('temperature', 0.7)
    
    @property
    def max_tokens(self) -> int:
        return self.llm_config.get('max_tokens', 2000)
    
    @property
    def docs(self) -> list:
        return self.llm_config.get('docs', [])
    
    @property
    def parameters(self) -> dict:
        return self.llm_config.get('parameters', {})

    class Config:
        env_file = ".env"

settings = Settings()
