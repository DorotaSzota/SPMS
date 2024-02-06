def individual_serial(elf) -> dict:
    return {
        "id": elf.id,
        "name": elf.name,
        "is_on_holidays": elf.is_on_holidays
    }

def list_serial(elves) -> list:
    return [individual_serial(elf) for elf in elves]