from fastapi import APIRouter, HTTPException, status, Response
from datetime import datetime, timedelta
from ..models import models
from ..helpers.helpers import database, get_password_hash, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login", response_model=models.Token)
async def login(
        form_data: models.Login
):
    user = authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
async def register(data: models.User, res: Response):
    email_exists = database["users"].find_one({"email": data.email})
    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already registered",
        )
    database["users"].insert_one({
        "date_created": datetime.now(),
        "password": get_password_hash(data.password),
        "email": data.email,
        "name": data.name,
        "lastname": data.lastname
    })
    res.status_code = 201
    return {"status": 201, "message": "account created successfully"}
