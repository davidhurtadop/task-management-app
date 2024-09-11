from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import ValidationError
from src.repositories.user import UserRepository
from src.models.user import UserModel
from src.services.auth import AuthService
from src.utils import response


class UserService:
    def __init__(self, db, logger):
        self.user_repo = UserRepository(db)
        self.logger = logger

    def register_user(self, user_data: UserModel):
        try:
            # Hash password
            user_data.password = generate_password_hash(user_data.password)
            user_id = self.user_repo.insert_one(user_data.model_dump())
            return response.create_response(201, "User Registered", f"User created with ID: {user_id}")
        except ValidationError as e:
            return response.create_response(400, "Validation Error", str(e))

    def login_user(self, email: str, password: str):
        user = self.user_repo.find_by_email(email)
        if user and check_password_hash(user["password"], password):
            token = AuthService.generate_token(user["id"])
            return response.create_response(200, "Login Successful", f"JWT: {token}")
        return response.create_response(401, "Login Failed", "Invalid credentials")
