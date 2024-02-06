from fastapi import APIRouter, HTTPException
from app.models import elf
from app.config.database import collection_name
from app.schema import schemas
from bson import ObjectId

router = APIRouter()


@router.get("/elves")
async def get_all_elves():
    elves = collection_name.find()
    return schemas.list_serial(elves)

@router.post("/")
async def add_elf(elf: elf.Elf):
    collection_name.insert_one(dict(elf))