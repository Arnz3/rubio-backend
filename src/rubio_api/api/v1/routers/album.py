from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session
from rubio_api.database import get_session

from rubio_api.api.v1.schemas.album import AlbumUpdate, AlbumCreate, AlbumRead 
from rubio_api.services import album as album_service


router = APIRouter(prefix="/album", tags=["album"])
sessionDep = Annotated[Session, Depends(get_session)]

@router.get("/", response_model=list[AlbumRead])
async def get_albums(session:sessionDep):
    return album_service.list_albums(session)


@router.post("/", response_model=AlbumRead)
async def create_album(session:sessionDep, payload:AlbumCreate):
    return album_service.create_album(session, payload)


@router.get("/{album_id}", response_model=AlbumRead)
async def get_single_album(session:sessionDep, album_id: int):
    return album_service.get_album_by_id(session, album_id)


@router.put("/{album_id}", response_model=AlbumRead)
async def update_album(session:sessionDep, album_id: int, payload:AlbumUpdate):
    album = album_service.get_album_by_id(session, album_id)
    if album is None:
        raise HTTPException(
            status_code=404,
            detail="Could not find album with this id"
        )
    return album_service.update_album(session, payload, album)


@router.delete("/{album_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(session:sessionDep, album_id: int):
    album = album_service.get_album_by_id(session, album_id)
    if album is None:
        raise HTTPException(
            status_code=404,
            detail="Could not find album with this id"
        )
    return album_service.remove_album(session, album)