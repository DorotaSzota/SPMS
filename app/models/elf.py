from pydantic import BaseModel

class Elf(BaseModel):
    id: int
    elf_name: str
    is_on_holidays: bool

def __init__(self, id: int, elf_name: str, is_on_holidays: bool):
    self.id = id
    self.elf_name = elf_name
    self.is_on_holidays = is_on_holidays