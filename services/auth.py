from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from database.database import DB as users_db
from jose import JWTError, jwt
from datetime import datetime, timedelta
#Kolya - TheBestPassword
#Jane - 123
#Olesya - ilovecats
ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")
pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=12)


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
    return payload

def authenticate_user(username: str, password: str):
    try:
        user = users_db.data[username]
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username",
        )
    if  not pwd_context.verify(password, users_db.data[username]["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect password",
        )
    return users_db.data[username]
