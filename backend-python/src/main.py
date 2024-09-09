from flask import Flask
from src.routes.user import UserRoutes
from src.routes.task import TaskRoutes
from src.clients.mongodb import MongoDbClient
from src.utils.config import settings
from src.utils.logging import LoggerFactory
from flask_jwt_extended import JWTManager


class TaskManagerApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.init_db()
        self.init_logger()
        self.init_jwt()
        self.register_blueprints()

    def configure_app(self):
        self.app.config.from_object(settings)
        
    
    def init_logger(self):
        self.logger = LoggerFactory(__name__,self.app.config["LOG_LEVEL"])
        self.app.logger = self.logger.get_logger()

    def init_db(self):
        self.mongo_client = MongoDbClient(self.app.config["MONGO_DB_URI"], self.app.config["MONGO_DB_NAME"])
        self.db = self.mongo_client.get_database()

    def init_jwt(self):
        JWTManager(self.app)

    def register_blueprints(self):
        self.app.register_blueprint(UserRoutes(self.db, self.app.logger).blueprint, url_prefix="/api/users")
        self.app.register_blueprint(TaskRoutes(self.db, self.app.logger).blueprint, url_prefix="/api/tasks")

    def run(self):
        print(self.app.url_map)
        self.app.run(debug=True)


if __name__ == "__main__":
    app = TaskManagerApp()
    app.run()
