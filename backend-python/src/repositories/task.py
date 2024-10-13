from src.repositories.base import BaseRepository
from uuid import UUID

class TaskRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, "tasks")

    def find_by_user(self, user_id: UUID):
        return list(self.collection.find({"user_id": str(user_id)}))
    
    def find_by_title(self, title: str):
        return list(self.collection.find({"title": title}))
    
    def find_by_id_user(self, task_id: UUID, user_id: UUID):
        return list(self.collection.find({"id": str(task_id), "user_id": str(user_id)}))
    
    def update_one_by_user(self, task_id: UUID, update_data: dict,user_id: UUID):
        result = self.collection.update_one({"id": str(task_id), "user_id": str(user_id)}, {"$set": update_data})
        return result
    
    def delete_one_by_user(self, task_id: UUID, user_id: UUID):
        result = self.collection.delete_one({"id": str(task_id), "user_id": str(user_id)})
        return result
