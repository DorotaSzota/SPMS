from fastapi import APIRouter
from app.models.package import Package
from app.config.database import collection_name
from app.schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_all_packages():
    packages = list_serial(collection_name.find())
    return packages

@router.post("/")
async def create_package(package: Package):
    collection_name.insert_one(dict(package))

@router.put("/{id}")
async def update_package(id: str, package: Package):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(package)})

@router.delete("/{id}")
async def delete_package(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})