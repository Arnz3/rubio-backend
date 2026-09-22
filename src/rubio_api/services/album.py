from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.models.album import Album
from rubio_api.api.v1.schemas.album import AlbumCreate, AlbumUpdate

def list_albums(session: Session) -> Sequence[Album]:
    return session.scalars(
        select(Album)
    ).all()


def create_album(session: Session, payload: AlbumCreate) -> Album:
    album = Album(**payload.model_dump())
    session.add(album)
    session.commit()
    session.refresh(album)
    return album


def get_album_by_id(session: Session, album_id: int) -> Album | None:
    return session.scalar(
        select(Album).where(Album.id == album_id)
    )


def update_album(session: Session, payload: AlbumUpdate, album:Album) -> Album:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(album, key, value)
    session.commit()
    session.refresh(album)
    return album


def remove_album(session: Session, album: Album) -> None:
    session.delete(album)
    session.commit()