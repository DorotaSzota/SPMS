from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:maslo1234@cluster0.5nrw8lo.mongodb.net/?retryWrites=true&w=majority")

db = client.package_manager_db
collection_name = db["package_manager"]