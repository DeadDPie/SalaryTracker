from fastapi import APIRouter
from api.users import router as user_router
from api.salary import router as salary_router
router = APIRouter(prefix='/api')

router.include_router(user_router)
router.include_router(salary_router)