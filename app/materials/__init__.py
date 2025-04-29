from app.materials.compliments.routers import router as compliments_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(
    compliments_router,
    prefix="/compliments",
    tags=["Compliments", ]
)
