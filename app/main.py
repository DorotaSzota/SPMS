from fastapi import FastAPI
from app.routers import elf_route, packages_route, pm_route
import ssl

app = FastAPI()

app.include_router(elf_route.router)
app.include_router(packages_route.router)
app.include_router(pm_route.router)
async def root():
    return {"message": "Alive and kicking!"}

# from pymongo.mongo_client import MongoClient
# uri = "mongodb+srv://admin:maslo1234@cluster0.5nrw8lo.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)
# # client = MongoClient(uri)
# try:
#     client.admin.command('ping')
#     print("Connected to the database")
# except Exception as e:
#     print("Connection error", e)