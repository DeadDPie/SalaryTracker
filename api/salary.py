from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from schemas.token_schema import Token
from services.auth import get_current_user
from schemas.salary_schema import Salary
from services import service

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.post('/token',
             response_model=Token,
)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect email or password')
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get(
    "/salary",
    status_code=200,
    response_model=Salary, summary="Зарплата",)
def get_salary(current_worker: dict = Depends(get_current_user)):
    return  {"salary": current_worker["salary"],
             "salary_rise_date": current_worker["salary_rise_date"]}#service.get_salary()

