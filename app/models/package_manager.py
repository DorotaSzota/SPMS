from pydantic import BaseModel
from app.models.status import Status
from app.models.elf import Elf
from app.models.package import Package


class PackageManager(BaseModel):
    id: int
    package_id: Package.id
    elf_id: Elf.id
    package_status: Status

    def __init__(self, id, package_id, elf_id, package_status):
        self.id = id
        self.package_id = package_id
        self.elf_id = elf_id
        self.package_status = package_status