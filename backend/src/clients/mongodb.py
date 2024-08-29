from pymongo import MongoClient as PyMongoClient


class MongoDbNotInitializedError(Exception):
    """MongoDB client is not initialized"""

class MongoClient:
    _instance = None

    def __init__(self, uri, db_name):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._instance = PyMongoClient(uri)[db_name]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise MongoDbNotInitializedError("MongoDB client is not initialized")
        return cls._instance
