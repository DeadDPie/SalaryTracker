from fastapi import APIRouter
from schemas.user_schema import User

router = APIRouter()


@router.get(
    "/users",
    status_code=200,
    response_model=list[User], )
def get_users():
    return user_service.get_users()

