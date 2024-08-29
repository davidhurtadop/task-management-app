import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    MONGO_URI: str = os.getenv("MONGO_DB_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DB_NAME")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL")


settings = Settings()