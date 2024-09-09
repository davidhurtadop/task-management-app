import os

from pydantic_settings import BaseSettings
from typing import ClassVar
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    MONGO_DB_URI: ClassVar[str] = os.getenv("MONGO_DB_URI")
    MONGO_DB_NAME: ClassVar[str] = os.getenv("MONGO_DB_NAME")
    LOG_LEVEL: ClassVar[str] = os.getenv("LOG_LEVEL")
    SECRET_KEY: ClassVar[str] = os.getenv("SECRET_KEY", )
    JWT_SECRET_KEY: ClassVar[str] = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION: ClassVar[str] = os.getenv("JWT_TOKEN_LOCATION")

settings = Settings()