from fastapi import APIRouter
from database.database import DB as data
from fastapi import APIRouter, HTTPException, security, Depends
from schemas import User
from schemas.token_schema import Token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")