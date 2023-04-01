from fastapi import FastAPI
from .endpoints import authenication, stock

app = FastAPI()
app.include_router(authenication.router)
app.include_router(stock.router)


@app.get("/")
@app.get("/info")
async def info():
    return
