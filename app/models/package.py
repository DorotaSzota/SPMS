from pydantic import BaseModel

class Package(BaseModel):
    package_name: str
    package_description: str