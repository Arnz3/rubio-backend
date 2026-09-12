from fastapi import APIRouter

from rubio_api.api.v1.routers import organization
from rubio_api.api.v1.routers import user

router = APIRouter()

router.include_router(organization.router)
router.include_router(user.router)
