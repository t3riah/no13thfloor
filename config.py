from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    APP_ENV: str = "development"
    SECRET_KEY: str = "changeme"
    DATABASE_URL: str = "sqlite:///./data/n13f.db"
    RESEND_API_KEY: str = ""
    STRIPE_SECRET_KEY: str = ""
    FROM_EMAIL: str = "audit@no13thfloor.org"
    REPORTS_DIR: str = "./reports"
    DATA_DIR: str = "./data"

    class Config:
        env_file = ".env"


settings = Settings()

# Ensure directories exist
Path(settings.REPORTS_DIR).mkdir(parents=True, exist_ok=True)
Path(settings.DATA_DIR).mkdir(parents=True, exist_ok=True)
