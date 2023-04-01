from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    email: str
    password: str


class User(BaseModel):
    password: str
    email: EmailStr
    name: str
    lastname: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class StockCategory(BaseModel):
    name: str
    type: str

    def __str__(self):
        return self.name


class StockItem(BaseModel):
    name: str
    category: str


class StockCategoryQuery(BaseModel):
    name: str
