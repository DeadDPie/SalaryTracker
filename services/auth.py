from typing import Optional, Union, Annotated
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status

from database.database import DB as data
from schemas import Salary
from schemas.token_schema import TokenData
from schemas.user_schema import User
from uuid import uuid4
from fastapi import Request, Response
from fastapi.responses import JSONResponse
import json
import jwt
from jose import JWTError, jwt
from datetime import datetime, timedelta



ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Auth:
    def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = get_user(data, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user
    def decode_access_token(token: str):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = decoded_token.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token")
            return username
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def login_for_access_token(username: str, password: str):
        if username == password:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token()
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")

auth = Auth()