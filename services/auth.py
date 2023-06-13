from typing import Optional, Union, Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from database.database import DB as database
from schemas import Salary
from schemas.token_schema import TokenData
from schemas.user_schema import User
from fastapi import Request, Response
from fastapi.responses import JSONResponse
import json
import jwt
from jose import JWTError, jwt
from datetime import datetime, timedelta



ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"
JWT_REFRESH_SECRET_KEY = 'JWT_REFRESH_SECRET_KEY'
REFRESH_TOKEN_EXPIRE_MINUTES = 60
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#class Auth:

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire_time = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode["exp"] = expire_time
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception
    return payload

# def login_for_access_token(username: str, password: str):
#     try:
#         user = database.data[username]
#         access_token = create_access_token(database.data)
#         if not pwd_context.verify(password, user["hashed_password"]):
#             return False
#         return {"access_token": access_token, "token_type": "bearer"}
#     except:
#         raise HTTPException(status_code=401, detail="There is no such worker")
#
# #auth = Auth()