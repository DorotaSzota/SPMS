from fastapi import APIRouter, HTTPException
from app.models.package_manager import PackageManager
from app.models.elf import Elf
from app.models.package import Package
from app.models.status import Status
from app.config.database import collection_name
from app.config.database import db
from bson import ObjectId

router = APIRouter()

def get_available_elves() -> list:
    available_elves = []
    elves = db.elves.find({"is_on_holidays": False})
    for elf in elves:
        if not collection_name.find_one({"elf_id": str(elf["_id"])}):
            available_elves.append(Elf(**elf))
    if not available_elves:
        raise HTTPException(status_code=404, detail="We run out of elves!")
    return available_elves

def save_package_manager(package_manager: PackageManager):
    collection_name.insert_one(package_manager.dict())

#wrzuciłam tu metody do szukania dostępnych elfów i zapisywania package_managera