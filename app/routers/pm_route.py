from fastapi import APIRouter, HTTPException
from app.models.package import Package
from app.models.elf import Elf
from app.config.database import collection_name
from bson import ObjectId

router = APIRouter()

