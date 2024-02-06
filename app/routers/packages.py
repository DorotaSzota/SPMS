from fastapi import APIRouter
from models.package import Package
from config.database import package_manager
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_all_packages():
    packages = list_serial(package_manager.find())
    return packages

@router.post("/")
async def create_package(package: Package):
    package_manager.insert_one(dict(package))

@router.put("/{id}")
async def update_package(id: str, package: Package):
    package_manager.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(package)})