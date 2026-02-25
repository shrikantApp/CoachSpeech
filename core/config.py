import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Coach Speech"
    # PostgreSQL Database URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://coach:FufeyH7ohb.r7aAedtc60G3@13.200.216.93:5432/coach")
    
    # JWT Secrets
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-keep-safe")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3000
    
    # OpenAI API Key
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "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")

settings = Settings()
