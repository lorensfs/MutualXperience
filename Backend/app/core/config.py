from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SECRET_KEY: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    ENVIRONMENT: str = "local"
    PROJECT_NAME: str = "MutualXPerience"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "/v1"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8000"]
    FRONTEND_HOST: str = "http://localhost:5173"
    LOG_LEVEL: str = "DEBUG"

    model_config = SettingsConfigDict(
        env_file=str(env_path),
        env_file_encoding="utf-8",
        extra="allow"
    )

settings = Settings()
