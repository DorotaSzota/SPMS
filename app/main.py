from fastapi import FastAPI
from app.routers import elf_route, packages_route, pm_route

app = FastAPI()

app.include_router(elf_route.router)
app.include_router(packages_route.router)
app.include_router(pm_route.router)
async def root():
    return {"message": "Alive and kicking!"}
