from fastapi import APIRouter
from api.users import router as user_router
from api.endpoints import router as endpoints_router
router = APIRouter(prefix='/api')

router.include_router(user_router)
router.include_router(endpoints_router)