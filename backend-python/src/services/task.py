from src.repositories.task import TaskRepository
from src.models.task import TaskModel
from src.utils import response
from uuid import UUID


class TaskService:
    def __init__(self, db, logger):
        self.task_repo = TaskRepository(db)
        self.logger = logger

    def create_task(self, task_data: TaskModel):
        task_dict = task_data.model_dump()
        task_id = self.task_repo.insert_one(task_dict)
        return response.create_response(201, "Task Created", f"Task created successfully with ID: {task_id}")

    def get_task_by_id(self, task_id: UUID):
        task = self.task_repo.find_by_id(task_id)
        if task:
            return response.create_response(200, "Task Retrieved", task)
        return response.create_response(404, "Task Not Found", f"No task found with ID: {task_id}")

    def update_task(self, task_id: UUID, update_data: dict):
        result = self.task_repo.update_one(task_id, update_data)
        if result.modified_count:
            return response.create_response(200, "Task Updated", f"Task {task_id} updated successfully")
        return response.create_response(404, "Task Not Found", f"No task found with ID: {task_id}")

    def delete_task(self, task_id: UUID):
        result = self.task_repo.delete_one(task_id)
        if result.deleted_count:
            return response.create_response(200, "Task Deleted", f"Task {task_id} deleted successfully")
        return response.create_response(404, "Task Not Found", f"No task found with ID: {task_id}")

    def get_tasks_by_user(self, user_id: UUID):
        tasks = self.task_repo.find_by_user(user_id)
        count_tasks = len(tasks)
        if count_tasks == 0:
            return response.create_response(200, "Tasks Not Found", f"No tasks found for user with ID: {user_id}")
        return response.create_response(200, "Tasks Retrieved", f"{count_tasks} Tasks found", tasks)
