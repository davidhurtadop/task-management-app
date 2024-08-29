import uuid

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskModel(BaseModel):
    id: Optional[uuid.UUID] = Field(None, alias="_id")
    title: str
    description: str
    create_date: datetime = Field(default_factory=datetime.now)
    due_date: datetime = Field(default_factory=datetime.now)
    start_date: datetime = Field(default_factory=datetime.now)
    status: str = "Pending"
    user_id: uuid.UUID

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        json_encoders = {
            uuid.UUID: str
        }