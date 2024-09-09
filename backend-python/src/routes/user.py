from flask import Blueprint, request
from src.services.user import UserService
from src.models.user import UserModel


class UserRoutes:
    def __init__(self, db, logger):
        self.user_service = UserService(db, logger)
        self.blueprint = Blueprint("user_routes", __name__)
        self.routes()

    def routes(self):
        @self.blueprint.route("/register", methods=["POST"])
        def register():
            data = request.get_json()
            user_data = UserModel(**data)
            return self.user_service.register_user(user_data)
            
        @self.blueprint.route("/login", methods=["POST"])
        def login():
            data = request.get_json()
            return self.user_service.login_user(data["email"], data["password"])
