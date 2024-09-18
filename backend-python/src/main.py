from flask import Flask
from src.routes.user import UserRoutes
from src.routes.task import TaskRoutes
from src.clients.mongodb import MongoDbClient
from src.utils.config import settings
from src.utils.logging import LoggerFactory
from flask_jwt_extended import JWTManager


app = Flask(__name__)

def configure_app():
    app.config.from_object(settings)
        
def init_logger():
    logger = LoggerFactory(__name__,app.config["LOG_LEVEL"])
    app.logger = logger.get_logger()

def init_db():
    db_uri = app.config["MONGO_DB_URI"]
    db_name = app.config["MONGO_DB_NAME"]
    mongo_client = MongoDbClient(db_uri, db_name)
    app.logger.debug(f"Connecting to MongoDB:{db_uri} - {db_name}")
    db = mongo_client.get_database()
    return db

def init_jwt():
    JWTManager(app)

def register_blueprints():
    db = init_db()
    app.register_blueprint(UserRoutes(db, app.logger).blueprint, url_prefix="/api/users")
    app.register_blueprint(TaskRoutes(db, app.logger).blueprint, url_prefix="/api/tasks")

def run():
    configure_app()
    init_logger()
    init_jwt()
    register_blueprints()
    
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == "__main__":
    run()
