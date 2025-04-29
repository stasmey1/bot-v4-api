from app.materials.compliments.routers import router as compliments_router
from app.materials.motivation_picture.routers import router as motivation_picture_router

from fastapi import APIRouter

router = APIRouter()

router.include_router(
    compliments_router,
    prefix="/compliments",
    tags=["Compliments", ]
)

router.include_router(
    motivation_picture_router,
    prefix="/motivation_picture",
    tags=["Motivation_picture", ]
)
