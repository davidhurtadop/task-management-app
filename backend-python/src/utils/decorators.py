from functools import wraps
from flask import request, jsonify
from src.services.auth import AuthService


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = AuthService.decode_token(token)
            if not data:
                return jsonify({"message": "Token is invalid or expired!"}), 401
            request.user_id = data['user_id']
        except Exception as e:
            return jsonify({"message": "An error occurred while validating the token."}), 401

        return f(*args, **kwargs)

    return decorated
