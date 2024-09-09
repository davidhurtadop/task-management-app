import uuid
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime, timezone


class UserModel(BaseModel):
    id: str = Field(default_factory = lambda: str(uuid.uuid4()))  # Automatically generates a UUID
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    create_date: Optional[datetime] = Field(default_factory = lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True

class UserDBModel(UserModel):
    # In MongoDB, password will be hashed
    password: str
