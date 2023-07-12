from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://filesautobot:filesautobot870@cluster0.qcxdkpw.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["channel-manager"]
        self.collection = self.db["channel_collection"]

    async def add_connection(self, channel_id, user_id):
        existing_channel_id = await self.get_channel_id(channel_id=channel_id)
        if existing_channel_id:
            return False

        document = {"channel_id": channel_id, "user_id": user_id}
        result = await self.collection.insert_one(document)
        return result.inserted_id

    async def get_channel_id(self, user_id=None, channel_id=None):
        query = {}
        if user_id:
            query["user_id"] = user_id
        if channel_id:
            query["channel_id"] = channel_id

        document = await self.collection.find_one(query)
        if document:
            return document["channel_id"]
        return None
