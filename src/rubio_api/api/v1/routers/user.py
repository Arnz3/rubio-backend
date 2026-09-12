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


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(session:sessionDep, payload:UserCreate):
    if user_service.get_user_by_email(session, payload.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    return user_service.add_user(session, payload)


@router.get("/{user_id}", response_model=UserRead)
async def get_single_user(session:sessionDep, user_id: int):
    user = user_service.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="No user with this Id exists"
        )
    return user

@router.put("/{user_id}", response_model=UserRead)
async def update_user(session:sessionDep, payload :UserUpdate, user_id: int):
    user = user_service.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user_service.update_user(session, payload, user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(session:sessionDep, user_id: int):
    user = user_service.get_user_by_id(session, user_id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user_service.delte_user(session, user)