"""
Rubio API - Entrypoint
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from rubio_api.config import settings

from rubio_api.api import v1
from rubio_api.api import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_TITLE,
        version=settings.API_VERSION,
        root_path="/api"
    )

    app.include_router(v1.router, prefix="/v1")
    app.include_router(health.router, prefix="/health")

    return app


app = create_app()