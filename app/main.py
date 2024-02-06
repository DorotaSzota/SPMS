from fastapi import FastAPI
from app.routers import elf_route, packages

app = FastAPI()

app.include_router(elf_route.router)
app.include_router(packages.router)
async def root():
    return {"message": "Alive and kicking!"}