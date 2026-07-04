from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from app.adapters.inbound.router import router as base_router
from app.config.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.settings = get_settings()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(base_router)
