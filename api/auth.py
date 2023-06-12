from typing import Annotated

from fastapi import APIRouter, HTTPException, security, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas import User
from schemas.token_schema import Token

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"

@router.post(
    "/token",
    response_model=Token,
    status_code=200,
    summary="Создание токена",
)
def create_token(
    form_data: security.OAuth2PasswordRequestForm = Depends(),
) -> dict:
    user = _control.authenticate_user(
        name=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=401, detail="Неверный логин или пароль")

    return  _control.create_token(user=user)
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user
