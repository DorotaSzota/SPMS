from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://admin:maslo1234@cluster0.5nrw8lo.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You're good to go!")
except Exception as e:
    print(e)