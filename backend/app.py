from  fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from config.config import COLLECTION_NAME, DB_NAME, MONGO_URI
from pymongo import MongoClient
from google.cloud import aiplatform


app=FastAPI()


class Question (BaseModell):
    title: str
    question=str

async def get_answer