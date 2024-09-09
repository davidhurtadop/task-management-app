class BaseRepository:
    def __init__(self, db, collection_name):
        self.collection = db[collection_name]

    def insert_one(self, data):
        return self.collection.insert_one(data).inserted_id

    def find_by_id(self, id):
        return self.collection.find_one({"id": str(id)})

    def update_one(self, id, data):
        return self.collection.update_one({"id": str(id)}, {"$set": data})

    def delete_one(self, id):
        return self.collection.delete_one({"id": str(id)})

    def find_all(self):
        return list(self.collection.find())
