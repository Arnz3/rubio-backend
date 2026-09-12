from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session
from rubio_api.database import get_session

from rubio_api.api.v1.schemas.user import UserCreate, UserRead, UserUpdate
from rubio_api.services import user as user_service

router = APIRouter(prefix="/user", tags=["user"])
sessionDep = Annotated[Session, Depends(get_session)]


@router.get("/", response_model=list[UserRead])
async def get_users(session:sessionDep):
    return user_service.users(session)


@router.post("/", response_model=UserRead)
async def create_user(session:sessionDep, payload:UserCreate):
    if user_service.get_user_by_email(session, payload.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    return user_service.add_user(session, payload)
