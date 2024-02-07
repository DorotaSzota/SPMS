from fastapi import APIRouter, HTTPException
from app.models.package import Package
from app.config.database import collection_name
from app.schema.schemas import list_serial_package
from bson import ObjectId

router = APIRouter()

@router.get("/packages/all")
async def get_all_packages():
    packages = list_serial_package(collection_name.find())
    return packages

@router.put("/packages/updt/{id}")
async def update_package(id: str, package: Package):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(package)})
@router.post("/packages/add")
async def create_package(package: Package):
    collection_name.insert_one(dict(package))
@router.delete("/packages/delete/{id}")
async def delete_package(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})