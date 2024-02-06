def individual_serial_elf(elf) -> dict:
    return {
        "id": str(elf["_id"]),
        "name": elf["elf_name"],
        "is_on_holidays": elf["is_on_holidays"]
    }


def list_serial_elf(elves) -> list:
    return [individual_serial_elf(elf) for elf in elves]


def individual_serial_package(package) -> dict:
    return {
        "id": str(package["_id"]),
        "name": package["package_name"],
        "description": package["package_description"],
    }


def list_serial_package(packages) -> list:
    return [individual_serial_package(package) for package in packages]


def individual_serial_pm(package_manager) -> dict:
    return {
        "id": package_manager.id,
        "package_id": package_manager.package_id,
        "elf_id": package_manager.elf_id,
        "status": package_manager.package_status,
    }


def list_serial_pm(packages) -> list:
    return [individual_serial_pm(package) for package in packages]
