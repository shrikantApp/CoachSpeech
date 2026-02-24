import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Coach Speech"
    # PostgreSQL Database URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/coachspeech")
    
    # JWT Secrets
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-keep-safe")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # OpenAI API Key
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "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")

settings = Settings()
