from fastapi import FastAPI
from pymongo import MongoClient
import helpers
import models

app = FastAPI()
mongo=MongoClient()

@app.post("/authenticate")
async def authenticate(login: models.Login):
    pass

@app.post("/register")
async def register():
    pass