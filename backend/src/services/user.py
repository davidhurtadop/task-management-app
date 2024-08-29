import uuid

from src.clients.mongodb import MongoClient
from src.utils.logging import Logger
from src.models.user import UserModel
from typing import Optional


class UserService:
    def __init__(self, mongo_client: MongoClient, logger: Logger):
        self.mongo_client = mongo_client
        self.logger = logger
        self.collection = self.mongo_client.db['users']

    def create_user(self, user: UserModel):
        user.id = uuid.uuid4()
        self.collection.insert_one(user.dict())
        return user

    def get_user_by_id(self, user_id: uuid.UUID) -> Optional[UserModel]:
        user_data = self.collection.find_one({'_id': user_id})
        if user_data:
            return UserModel(**user_data)
        return None

    def get_user_by_username(self, username: str) -> Optional[UserModel]:
        user_data = self.collection.find_one({'username': username})
        if user_data:
            return UserModel(**user_data)
        return None

    def update_user(self, user_id: uuid.UUID, user: UserModel):
        self.collection.update_one({'_id': user_id}, {'$set': user.dict(exclude={'id'})})
        return self.get_user_by_id(user_id)

    def delete_user(self, user_id: uuid.UUID):
        self.collection.delete_one({'_id': user_id})
        return True
