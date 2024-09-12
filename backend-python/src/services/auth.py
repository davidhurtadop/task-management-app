import jwt
from datetime import datetime, timezone, timedelta
from flask import current_app


class AuthService:
    @staticmethod
    def generate_token(user_id):
        payload = {
            "user_id": str(user_id),
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        }
        return jwt.encode(payload, current_app.config.get("JWT_SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, current_app.config.get("JWT_SECRET_KEY"), algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
