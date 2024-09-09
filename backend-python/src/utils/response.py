from flask import jsonify


class APIResponse:
    @staticmethod
    def create_response(status_code: int, message: str, description: str):
        response = {
            "status-code": status_code,
            "message": message,
            "description": description
        }
        return jsonify(response), status_code
