from database.database import DB as users_db
from fastapi import APIRouter, HTTPException, Depends
from schemas import Salary
from schemas.token_schema import Token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from services.auth import get_current_user, create_access_token, authenticate_user

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES=30
SECRET_KEY="wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM="HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post('/token',
             response_model=Token,
             status_code=200,
             summary="Создание токена"
)
def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect username or password')
    access_token = create_access_token(user=user)
    return Token(access_token= access_token["access_token"], token_type= "bearer")

@router.get(
    "/salary",
    status_code=200,
    response_model=Salary,
    summary="Зарплата"
)
def get_salary(current_worker: dict = Depends(get_current_user)):
    return  Salary(salary=current_worker["salary"],salary_rise_date =current_worker["salary_rise_date"])

