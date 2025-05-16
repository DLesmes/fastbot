from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastBot"
    debug: bool = True

settings = Settings()
