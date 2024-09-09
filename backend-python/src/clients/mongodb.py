from pymongo import MongoClient


class MongoDbClient:
    __instance = None

    @staticmethod
    def get_instance(uri=None, db_name=None):
        """Get the singleton instance of the MongoDB client.

        Args:
            uri (str, optional): The MongoDB connection URI. 
                                  If not provided, uses existing instance.
            db_name (str, optional): The database name. 
                                     If not provided, uses existing instance.

        Returns:
            MongoDbClient: The singleton instance.

        Raises:
            ValueError: If uri or db_name are not provided on the first call.
        """
        if MongoDbClient.__instance is None:
            if not uri or not db_name:
                raise ValueError("URI and database name are required for initialization.")
            MongoDbClient(uri, db_name)
        return MongoDbClient.__instance

    def __init__(self, uri, db_name):
        """Initialize the singleton instance."""
        if MongoDbClient.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.client = MongoClient(uri)
            self.database = self.client.get_database(db_name)
            MongoDbClient.__instance = self

    def get_database(self):
        """Get the database object."""
        return self.database

    def close(self):
        """Close the MongoDB client connection."""
        if self.client:
            self.client.close()
            self.client = None
            MongoDbClient.__instance = None
