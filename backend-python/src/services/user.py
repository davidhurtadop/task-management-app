import re

from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import ValidationError
from flask import jsonify
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
            if not user_data.email or not re.match(r"[^@]+@[^@]+\.[^@]+", user_data.email):
                return response.create_response(400, "invalid mail", "Invalid email address")

            if not user_data.password or not is_strong_password(user_data.password):
                return response.create_response(400, "invalid password", "Password must meet the requirements")
            
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


def is_strong_password(password):
    """Checks if a password meets the requirements."""
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(re.match(regex, password))
