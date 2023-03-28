from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username:str
    date_registered:str