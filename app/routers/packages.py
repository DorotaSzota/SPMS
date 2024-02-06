from fastapi import APIRouter
from models.package import Package
from config.database import package_manager
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()