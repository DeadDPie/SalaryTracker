from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

users_db = {
    "user1": {
        "id": "3beeb1f1-2ec2-475e-bd38-4952f2e4235b",
        "email": "rtybjn@mail.ru",
        "username": "Kolya",
        "hashed_password": "UaVS",
        "salary": "60000",
    "salary_rise_date": "2023-10-22"},
    "user2": {
        "id": "2831e77b-463d-4678-b261-cb52684db28a",
        "email": "qwerty@mail.ru",
        "username": "Jane",
        "hashed_password": "hgff",
        "salary": "20000",
    "salary_rise_date": "2023-11-22"},

    "user3": {
        "id": "f12fa086-3655-425a-8c82-86d7c815c021",
        "email": "sefdg@mail.ru",
        "username": "Olesya",
        "hashed_password": "UaVnbvS",
        "salary": "500000",
        "salary_rise_date": "2023-09-22"
    }
}

def authenticate_user(username, password):
    if username in users_db and users_db[username]['hashed_password'] == password:
        return users_db[username]

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

@router.post('/token',
             summary="te работников")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/salary',
            summary="tessss работников")
async def get_salary(current_user: dict = Depends(get_current_user)):
    return  {"salary": current_user["salary"]}