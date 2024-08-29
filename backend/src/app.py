# app.py
from flask import Flask
from flask_restx import Api
from src.routes import register_routes
from src.clients.mongodb import MongoClient
from src.config import settings
from src.utils.logging import Logger


class TaskManagerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, version='1.0', title='Task Management API',
                       description='API for managing tasks and users')
        
        # Create the logger instance here
        self.logger = Logger(name="TaskManagerApp")

        try:
            self.mongo_client = MongoClient(settings.MONGO_URI, settings.MONGO_DATABASE)
        except Exception as e:
            self.logger.error(f"Error connecting to MongoDB: {e}")
            raise e  # Re-raise the exception to stop app initialization
        register_routes(self.api, self.mongo_client, self.logger)

    def run(self):
        self.logger.info("Starting Task Manager App")
        self.app.run(debug=True)

if __name__ == '__main__':
    app = TaskManagerApp()
    app.run()
