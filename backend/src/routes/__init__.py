from flask_restx import Api
from . import task as TaskRoutes
from . import user as UserRoutes


def register_routes(api: Api, mongo_client, logger):
    """Register all namespaces and inject dependencies here."""
    api.add_namespace(TaskRoutes(mongo_client, logger).namespace)
    api.add_namespace(UserRoutes(mongo_client, logger).namespace)
