import uuid

from flask_restx import Namespace, Resource, reqparse
from src.models.task import TaskModel
from src.services.task import TaskService


class TaskRoute:
    def __init__(self, mongo_client, logger):
        self.namespace = Namespace('tasks', description='Task related operations')
        self.task_service = TaskService(mongo_client, logger)
        self.register_routes()

    def register_routes(self):
        @self.namespace.route('/')
        class TaskList(Resource):
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help='Task title')
            parser.add_argument('description', type=str, help='Task description')
            parser.add_argument('due_date', type=str, help='Task due date (YYYY-MM-DD)')
            parser.add_argument('start_date', type=str, help='Task start date (YYYY-MM-DD)')
            parser.add_argument('status', type=str, help='Task status')
            parser.add_argument('user_id', type=str, required=True, help='User ID')

            @self.namespace.doc('list_tasks')
            def get(self):
                """List all tasks"""
                tasks = self.task_service.get_all_tasks()
                return [task.dict() for task in tasks]

            @self.namespace.doc('create_task')
            @self.namespace.expect(parser)
            def post(self):
                """Create a new task"""
                data = self.parser.parse_args()
                new_task = TaskModel(**data)
                created_task = self.task_service.create_task(new_task)
                return created_task.dict(), 201

        @self.namespace.route('/<string:task_id>')
        class TaskById(Resource):
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='Task title')
            parser.add_argument('description', type=str, help='Task description')
            parser.add_argument('due_date', type=str, help='Task due date (YYYY-MM-DD)')
            parser.add_argument('start_date', type=str, help='Task start date (YYYY-MM-DD)')
            parser.add_argument('status', type=str, help='Task status')
            parser.add_argument('user_id', type=str, help='User ID')

            @self.namespace.doc('get_task_by_id')
            def get(self, task_id: str):
                """Get a task by ID"""
                task = self.task_service.get_task_by_id(uuid.UUID(task_id))
                if task:
                    return task.dict()
                else:
                    self.namespace.abort(404, f"Task with ID {task_id} not found")

            @self.namespace.doc('update_task')
            @self.namespace.expect(parser)
            def put(self, task_id: str):
                """Update a task"""
                data = self.parser.parse_args()
                updated_task = self.task_service.update_task(uuid.UUID(task_id), TaskModel(**data))
                if updated_task:
                    return updated_task.dict()
                else:
                    self.namespace.abort(404, f"Task with ID {task_id} not found")

            @self.namespace.doc('delete_task')
            def delete(self, task_id: str):
                """Delete a task"""
                success = self.task_service.delete_task(uuid.UUID(task_id))
                if success:
                    return '', 204
                else:
                    self.namespace.abort(404, f"Task with ID {task_id} not found")
