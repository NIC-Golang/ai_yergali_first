from pymongo import MongoClient

class MongoTagRepository:
    def __init__(self, uri: str, database: str, collection: str):
        client = MongoClient(uri)
        self.collection = client[database][collection]

    def save_tags(self, book_id: int, tags: list):
        self.collection.update_one(
            {"book_id": book_id},
            {"$set": {"tags": tags}},
            upsert=True
        )