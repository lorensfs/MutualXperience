from pydantic import AnyUrl, BeforeValidator, Field, computed_field, model_validator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Any
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"

def parse_cors(cors_string: Any) -> list[str] | str:
    if isinstance(cors_string, str) and not cors_string.startswith("["):
        return [i.strip() for i in cors_string.split(",")]
    elif isinstance(cors_string, list | str):
        return cors_string
    raise ValueError(cors_string)

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
    LOG_FORMAT: str = "%(levelname)s: %(message)s\n\t%(name)s | %(asctime)s"

    EMAILS_FROM_EMAIL: str | None = None
    EMAILS_FROM_NAME: str | None = None

    SMTP_TLS: bool = False
    SMTP_SSL: bool = False
    SMTP_PORT: int = 1025
    SMTP_HOST: str = "localhost"
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEST_USER: str | None = "test@example.com"

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).strip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]

    @computed_field
    @property
    def SQLMODEL_DATABASE_URI(self) -> str:
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=str(env_path),
        env_file_encoding="utf-8",
        extra="allow"
    )

settings = Settings()
