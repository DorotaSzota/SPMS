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