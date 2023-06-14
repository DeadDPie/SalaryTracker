# from typing import Optional, Union, Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from database.database import DB as users_db
from jose import JWTError, jwt
from datetime import datetime, timedelta


ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(user: dict)->dict:
    user["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encoded_jwt = jwt.encode(user, SECRET_KEY, algorithm=ALGORITHM)
    return dict(access_token=encoded_jwt, token_type="bearer")
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Login or password is uncorrect or JWT has run out of time",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    print(payload)
    return payload

def authenticate_user(username: str, password: str):
    try:
        user = users_db.data[username]
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username",
        )
    if password != users_db.data[password]:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password",
        )
    #if not password_context.verify(password, user["hashed_password"]):#TODO:hashed password
    #     return False
    return users_db.data[username]
