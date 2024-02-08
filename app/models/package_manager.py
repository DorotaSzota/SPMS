from pydantic import BaseModel
from bson import ObjectId


class PackageManager(BaseModel):
    package_id: str
    elf_id: str
    address: str
