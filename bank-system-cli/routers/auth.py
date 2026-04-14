from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from data_manager import load_data, save_data
from models import User
from utils import hash_password
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

data = load_data()

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class CreateAccountRequest(BaseModel):
    username: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/create-account")
def create_account(request: CreateAccountRequest):
    if request.username in data["users"]:
        return {"error": "Username already exists"}

    user = User(request.username, hash_password(request.password))

    data["users"][request.username] = user.to_dict()
    save_data(data)

    return {"message": "Account created successfully"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username not in data["users"]:
        raise HTTPException(status_code=400, detail="User not found")

    user_data = data["users"][username]

    if user_data["password"] != hash_password(password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"sub": username})

    return {"access_token": token, "token_type": "bearer"}