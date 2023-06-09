from fastapi import APIRouter
from schemas.salary_schema import Salary

router = APIRouter()


@router.get(
    "/salary",
    status_code=200,
    response_model=list[Salary], )
def get_salary():
    return user_service.get_salary()

