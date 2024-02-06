from pydantic import BaseModel

class Elf(BaseModel):
    elf_name: str
    is_on_holidays: bool