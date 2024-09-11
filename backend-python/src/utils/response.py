from flask import jsonify
from dataclasses import dataclass
from bson.objectid import ObjectId


@dataclass
class Response:
    status_code: int
    message: str
    description: str
    details: any = None


def create_response(status_code: int, message: str, description: str, details: any = None):
    if isinstance(details, list):
        details = [{k: str(v) if isinstance(v, ObjectId) else v for k, v in d.items()} for d in details]
    elif isinstance(details, dict):
        details = {k: str(v) if isinstance(v, ObjectId) else v for k, v in details.items()}
    elif isinstance(details, ObjectId):
        details = str(details)

    response = Response(status_code, message, description, details)
    return jsonify(response), status_code