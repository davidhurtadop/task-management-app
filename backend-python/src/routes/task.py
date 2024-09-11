from flask import Blueprint, request
from src.services.task import TaskService
from src.models.task import TaskModel
from src.utils.decorators import token_required


class TaskRoutes:
    def __init__(self, db, logger):
        self.task_service = TaskService(db, logger)
        self.blueprint = Blueprint("task_routes", __name__)
        self.routes()

    def routes(self):
        @self.blueprint.route("/", methods=["POST"])
        @token_required
        def create_task():
            data = request.get_json()
            data["user_id"] = request.user_id
            task_data = TaskModel(**data)
            return self.task_service.create_task(task_data)

        @self.blueprint.route("/<task_id>", methods=["GET"])
        @token_required
        def get_task(task_id):
            return self.task_service.get_task_by_id(task_id)

        @self.blueprint.route("/<task_id>", methods=["PUT"])
        @token_required
        def update_task(task_id):
            update_data = request.get_json()
            return self.task_service.update_task(task_id, update_data)

        @self.blueprint.route("/<task_id>", methods=["DELETE"])
        @token_required
        def delete_task(task_id):
            return self.task_service.delete_task(task_id)

        @self.blueprint.route("/user/<user_id>", methods=["GET"])
        @token_required
        def get_tasks_by_user(user_id):
            return self.task_service.get_tasks_by_user(user_id)
