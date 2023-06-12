from typing import List

from fastapi import APIRouter
from schemas.user_schema import User
from services import service, auth

router = APIRouter()


@router.get(
    "/users",
    status_code=200,
    response_model=list[User],
    summary="Список работников",
)
def get_users()->List[User]:
    return service.get_users()

@router.post("/token",
status_code=200,
    #response_model=Token,
#summary="Создание токена"
)
def creare_token():
    return auth.create_access_token()