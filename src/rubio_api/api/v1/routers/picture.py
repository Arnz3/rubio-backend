from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session
from rubio_api.database import get_session

from rubio_api.api.v1.schemas.picture import PictureUpdate, PictureCreate, PictureRead
from rubio_api.services import picture as picture_service


router = APIRouter(prefix="/picture", tags=["picture"])
sessionDep = Annotated[Session, Depends(get_session)]

@router.get("/", response_model=list[PictureRead])
async def get_all_pictures(session:sessionDep):
    return picture_service.list_pictures(session)


@router.post("/", response_model=PictureRead)
async def create_picture(session:sessionDep, payload:PictureCreate):
    return picture_service.create_picture(session, payload)


@router.get("/{pic_id}", response_model=PictureRead)
async def get_pic_by_id(session:sessionDep, pic_id: int):
    pic = picture_service.get_pic_by_id(session, pic_id)
    if pic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Picture with this id not found"
        )
    return pic


@router.put("/{pic_id}", response_model=PictureRead)
async def update_pic(session:sessionDep, payload:PictureUpdate, pic_id: int):
    pic = picture_service.get_pic_by_id(session, pic_id)
    if pic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Picture with this id not found"
        )
    return picture_service.update_pic(session, pic, payload)


@router.delete("/{pic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pic(session: sessionDep, pic_id: int):
    pic = picture_service.get_pic_by_id(session, pic_id)
    if pic is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Picture with this id not found"
        )
    return picture_service.delete_pic(session, pic)
