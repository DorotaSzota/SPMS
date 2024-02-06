from pydantic import BaseModel

class Package(BaseModel):
    id: int
    package_name: str
    package_description: str

    def __init__(self, id, package_name, package_description):
        self.id = id
        self.package_name = package_name
        self.package_description = package_description