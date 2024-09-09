from src.repositories.base import BaseRepository
from uuid import UUID

class TaskRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, "tasks")

    def find_by_user(self, user_id: UUID):
        return list(self.collection.find({"user_id": str(user_id)}))
    
    def find_by_title(self, title: str):
        return list(self.collection.find({"title": title}))
