import uuid
import datetime

from pydantic import BaseModel, validator, Field
from typing import Optional


class UserModel(BaseModel):
    id: Optional[uuid.UUID] = Field(None, alias="_id")
    username: str
    email: str
    password: str
    create_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    @validator('email')
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        return value

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        json_encoders = {
            uuid.UUID: str
        }
