from src.repositories.base import BaseRepository
from uuid import UUID

class UserRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, "users")

    def find_by_email(self, email: str):
        return self.collection.find_one({"email": email})

    def find_by_id(self, user_id: UUID):
        return self.collection.find_one({"id": str(user_id)})
