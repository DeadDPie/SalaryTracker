from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from schemas.salary_schema import Salary
from services import service

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.get(
    "/salary",
    status_code=200,
    response_model=list[Salary], summary="Зарплата",)
def get_salary(token: Annotated[str, Depends(oauth2_scheme)]):
    return  {"token": token}#service.get_salary()

