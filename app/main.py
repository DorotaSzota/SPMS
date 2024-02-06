from fastapi import FastAPI

app = FastAPI()

from pymongo.mongo_client import MongoClient
url = 
client = MongoClient(url)
try:
    client.admin.command('ping'
    print("Pinged your deployment. You're good to go!"))
except Exception as e:
    print(e)