from pydantic import BaseModel

class Elf(BaseModel):
    id: int
    name: str
    is_on_holidays: bool

    class Config:
        orm_mode = True