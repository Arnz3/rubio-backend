from fastapi import APIRouter

from rubio_api.api.v1.routers import organization

router = APIRouter()

router.include_router(organization.router)