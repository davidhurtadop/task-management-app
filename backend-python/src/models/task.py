import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone


class TaskModel(BaseModel):
    id: str = Field(default_factory = lambda: str(uuid.uuid4()))  # Automatically generates a UUID
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = None
    create_date: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    status: str = Field(default="pending",pattern="^(pending|in-progress|completed)$")
    user_id: str  # Foreign key to the User

    class Config:
        from_attributes = True
