
from fastapi import APIRouter

router = APIRouter(prefix="/organization", tags=["organization"])

@router.get("/")
async def get_organizations():
    return