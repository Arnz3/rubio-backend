from fastapi import APIRouter

from rubio_api.api.v1.routers import organization
from rubio_api.api.v1.routers import event
from rubio_api.api.v1.routers import user
from rubio_api.api.v1.routers import album
from rubio_api.api.v1.routers import picture

router = APIRouter()

router.include_router(organization.router)
router.include_router(event.router)
router.include_router(user.router)
router.include_router(album.router)
router.include_router(picture.router)