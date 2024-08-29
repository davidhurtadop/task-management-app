import uuid

from src.clients.mongodb import MongoClient
from src.utils.logging import Logger
from src.clients.mongodb import MongoClient
from src.models.task import TaskModel
from typing import Optional


class TaskService:
    def __init__(self, mongo_client: MongoClient, logger: Logger):
        self.mongo_client = mongo_client
        self.logger = logger
        self.collection = self.mongo_client.db['tasks']

    def create_task(self, user: TaskModel):
        user.id = uuid.uuid4()
        self.collection.insert_one(user.dict())
        return user

    def get_task_by_id(self, task_id: uuid.UUID) -> Optional[TaskModel]:
        user_data = self.collection.find_one({'_id': task_id})
        if user_data:
            return TaskModel(**user_data)
        return None

    def get_task_by_title(self, title: str) -> Optional[TaskModel]:
        user_data = self.collection.find_one({'title': title})
        if user_data:
            return TaskModel(**user_data)
        return None

    def update_task(self, task_id: uuid.UUID, user: TaskModel):
        self.collection.update_one({'_id': task_id}, {'$set': user.dict(exclude={'id'})})
        return self.get_task_by_id(task_id)

    def delete_task(self, task_id: uuid.UUID):
        self.collection.delete_one({'_id': task_id})
        return True
