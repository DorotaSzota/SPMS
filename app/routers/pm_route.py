from fastapi import APIRouter, HTTPException
from app.models.package_manager import PackageManager
from app.models.package import Package
from app.models.elf import Elf
from app.models.status import Status
from app.config.database import collection_name
from app.crud.pm_crud import get_available_elves, save_package_manager
from bson import ObjectId

router = APIRouter()

@router.post("/package_manager/assign_elf_to_package/{package_id}")
async def assign_elf_to_package(package_id: str, package: Package):

    available_elves = get_available_elves()

    if package.elf_id:
        raise HTTPException(status_code=400, detail="Package already has an assigned elf")

    for elf in available_elves:
        if not elf.is_on_holidays:
            package_manager = PackageManager(
                package_id=package.id,
                elf_id=elf.id,
                package_status=Status.ASSIGNED
            )
            save_package_manager(package_manager)
            return {"message": f"Elf {elf.id} assigned to package {package.id}"}

    raise HTTPException(status_code=400, detail="We run out of elves!")

@router.get("/package_manager/packages_without_elf")
async def get_packages_without_elf():
    packages = collection_name.find({"elf_id": {"$exists": False}})
    return [Package(**package) for package in packages]

# to powinno przypisywać paczki do elfów, ale nie działa, oby przez problem z id, ale to może być myślenie życzeniowe
# czemu nie robimy tego na bazie relacyjnej? XD