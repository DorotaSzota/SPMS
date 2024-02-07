from pydantic import BaseModel

class Elf(BaseModel):
    id: int
    elf_name: str
    is_on_holidays: bool