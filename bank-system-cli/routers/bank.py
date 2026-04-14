from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from jose import jwt

from data_manager import load_data, save_data
from models import User
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

data = load_data()

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class TransactionRequest(BaseModel):
    amount: int

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/deposit")
def deposit(request: TransactionRequest, username: str = Depends(get_current_user)):
    user_data = data["users"][username]

    user = User(
        username,
        user_data["password"],
        user_data["balance"],
        user_data["history"]
    )

    if not user.deposit(request.amount):
        return {"error": "Invalid amount"}

    data["users"][username] = user.to_dict()
    save_data(data)

    return {"message": "Deposit successful", "balance": user.balance}