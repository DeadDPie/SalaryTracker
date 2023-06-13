from typing import Annotated
from services.auth import get_current_user

from fastapi import APIRouter, HTTPException, security, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database.database import DB as data
from schemas import User
from schemas.token_schema import Token
from fastapi import FastAPI, status, HTTPException, Depends
from services.auth import get_hashed_password,create_access_token,create_refresh_token,verify_password

from uuid import uuid4

from services.auth import verify_password

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.post(
    "/token",
    response_model=Token,
    status_code=200,
    summary="Создание токена",
)
def create_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
) -> dict:
    if not (data.data.username==form_data.username and data.data.password==form_data.password):
        raise HTTPException(
            status_code=401, detail="Неверный логин или пароль")

    return create_token(user=data.data)

#
@router.post('/login', summary="Create access and refresh tokens for user", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = data.data.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }

@router.get('/me', summary='Get details of currently logged in user', response_model=User)
async def get_me(user: User = Depends(get_current_user)):
    return user