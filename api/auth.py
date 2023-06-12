from typing import Annotated

from fastapi import APIRouter, HTTPException, security, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database.database import DB as data
from schemas import User
from schemas.token_schema import Token

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

