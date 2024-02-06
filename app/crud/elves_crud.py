# from fastapi import HTTPException
# from pymongo import MongoClient
# from app import models, schema
# import app.config

# def get_all_elves():
#     elves = app.config.database.collection_name.find()
#     return schema.schemas.list_serial(elves)