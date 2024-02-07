from pydantic import BaseModel

class Package(BaseModel):
    id: int
    package_name: str
    package_description: str
