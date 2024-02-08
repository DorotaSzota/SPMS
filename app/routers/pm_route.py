from fastapi import APIRouter, HTTPException
from app.models.package_manager import PackageManager
from app.schema.schemas import list_pms
from app.config.database import collection_name


router = APIRouter()

@router.get("/ackage_manager/all")
async def get_package_managers():
    try:
        package_managers = list_pms(collection_name.find())
        return package_managers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/package_manager/create")
async def create_package_manager(package_manager: PackageManager):
    collection_name.insert_one(dict(package_manager))
