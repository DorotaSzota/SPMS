from pydantic import BaseModel
from app.models.status import Status
from app.models.elf import Elf
from app.models.package import Package
from app.routers.elf_route import ObjectId as elf_id
from app.routers.packages_route import ObjectId as package_id

class PackageManager(BaseModel):
    package_id: package_id
    elf_id: elf_id
    package_status: Status

# nie jestem pewna tych id :(