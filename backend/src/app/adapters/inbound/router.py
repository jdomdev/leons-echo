from fastapi import APIRouter

from app.adapters.inbound.health import router as health_router

router = APIRouter()
router.include_router(health_router)
