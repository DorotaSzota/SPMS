from pydantic import BaseModel
from app.models.status import Status
from app.models.elf import Elf
from app.models.package import Package


class PackageManager(BaseModel):
    package_id: Package.id
    elf_id: Elf.id
    package_status: Status