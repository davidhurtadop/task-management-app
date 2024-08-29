import uuid

from flask_restx import Namespace, Resource, reqparse
from src.models.user import UserModel
from src.services.user import UserService


class UserRoutes:
    def __init__(self, mongo_client, logger):
        self.namespace = Namespace('users', description='User related operations')
        self.user_service = UserService(mongo_client, logger)
        self.register_routes()

    def register_routes(self):
        @self.namespace.route('/')
        class UserList(Resource):
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True, help='User username')
            parser.add_argument('email', type=str, required=True, help='User email')
            parser.add_argument('password', type=str, required=True, help='User password')

            @self.namespace.doc('list_users')
            def get(self):
                """List all users"""
                users = self.user_service.get_all_users()
                return [user.dict() for user in users]

            @self.namespace.doc('create_user')
            @self.namespace.expect(self.parser)
            def post(self):
                """Create a new user"""
                data = self.parser.parse_args()
                new_user = UserModel(**data)
                created_user = self.user_service.create_user(new_user)
                return created_user.dict(), 201

        @self.namespace.route('/<string:user_id>')
        class UserById(Resource):
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='User username')
            parser.add_argument('email', type=str, help='User email')
            parser.add_argument('password', type=str, help='User password')

            @self.namespace.doc('get_user_by_id')
            def get(self, user_id: str):
                """Get a user by ID"""
                user = self.user_service.get_user_by_id(uuid.UUID(user_id))
                if user:
                    return user.dict()
                else:
                    self.namespace.abort(404, f"User with ID {user_id} not found")

            @self.namespace.doc('update_user')
            @self.namespace.expect(self.parser)
            def put(self, user_id: str):
                """Update a user"""
                data = self.parser.parse_args()
                updated_user = self.user_service.update_user(uuid.UUID(user_id), UserModel(**data))
                if updated_user:
                    return updated_user.dict()
                else:
                    self.namespace.abort(404, f"User with ID {user_id} not found")

            @self.namespace.doc('delete_user')
            def delete(self, user_id: str):
                """Delete a user"""
                success = self.user_service.delete_user(uuid.UUID(user_id))
                if success:
                    return '', 204
                else:
                    self.namespace.abort(404, f"User with ID {user_id} not found")
