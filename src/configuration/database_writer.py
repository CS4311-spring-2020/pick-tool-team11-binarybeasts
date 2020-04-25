import pymongo


class DatabaseWriter:

    # Possible connection names
    COLLECTION_TEAM = "team"
    COLLECTION_EVENT = "event"
    COLLECTION_DIRECTORY = "directory"
    COLLECTION_VECTOR = "vectors"
    COLLECTION_ICON = "icons"

    @staticmethod
    def connect_to_database():
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["pick_tool"]
        return database

    @staticmethod
    def write_dict_to_collection(dict_to_write, collection_name):
        database = DatabaseWriter.connect_to_database()
        collection = database[collection_name]
        if (collection_name == DatabaseWriter.COLLECTION_TEAM or
                collection_name == DatabaseWriter.COLLECTION_EVENT or
                collection_name == DatabaseWriter.COLLECTION_DIRECTORY):
            collection.delete_many({})
        collection.insert_one(dict_to_write)

    @staticmethod
    def print_collection(collection_name):
        print("Documents in " + collection_name + " collection:")
        for document in DatabaseWriter.connect_to_database()[collection_name].find():
            print(document)
