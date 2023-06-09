from fastapi import APIRouter
from schemas.salary_schema import Salary
from services import service

router = APIRouter()


@router.get(
    "/salary",
    status_code=200,
    response_model=list[Salary], )
def get_salary():
    return service.get_salary()

