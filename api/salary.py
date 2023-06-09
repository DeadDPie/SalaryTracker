from fastapi import APIRouter
from schemas.salary_schema import Salary
from services import service

router = APIRouter()


@router.get(
    "/salary",
    status_code=200,
    response_model=list[Salary], summary="Анонимный список зарплат",)
def get_salary():
    return service.get_salary()

