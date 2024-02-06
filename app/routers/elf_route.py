from fastapi import APIRouter, HTTPException
from app.models.elf import Elf
from app.config.database import collection_name
from app.schema.schemas import list_serial_elf
from bson import ObjectId

router = APIRouter()

@router.get("/elves")
async def get_all_elves():
    elves = list_serial_elf(collection_name.find())
    return elves

@router.post("/")
async def add_elf(elf: Elf):
    collection_name.insert_one(dict(elf))

@router.put("/{id}")
async def update_elf(id: str, elf : Elf):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(elf)})

@router.delete("/{id}")
async def delete_elf(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})