from fastapi import FastAPI
from app.routers import elf_route

app = FastAPI()

app.include_router(elf_route.router)

async def root():
    return {"message": "Alive and kicking!"}