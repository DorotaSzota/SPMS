def individual_serial(elf) -> dict:
    return {
        "id": elf.id,
        "name": elf.elf_name,
        "is_on_holidays": elf.is_on_holidays
    }

def list_serial(elves) -> list:
    return [individual_serial(elf) for elf in elves]

def individual_serial(package) -> dict:
    return {
        "id": package.id,
        "name": package.package_name,
        "description": package.package_description,
    }

def list_serial(packages) -> list:
    return [individual_serial(package) for package in packages]

def individual_serial(package_manager) -> dict:
    return {
        "id": package_manager.id,
        "package_id": package_manager.package_id,
        "elf_id": package_manager.elf_id,
        "status": package_manager.package_status,
    }

def list_serial(packages) -> list:
    return [individual_serial(package) for package in packages]