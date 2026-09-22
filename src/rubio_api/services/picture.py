from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.models.picture import Picture
from rubio_api.api.v1.schemas.picture import PictureCreate, PictureUpdate

def list_pictures(session: Session) -> Sequence[Picture]:
    return session.scalars(
        select(Picture)
    ).all()


def create_picture(session: Session, payload: PictureCreate) -> Picture:
    pic = Picture(**payload.model_dump())
    pic.full_url = "generate full url here"
    pic.thumb_url = "generate thumb here"
    session.add(pic)
    session.commit()
    session.refresh(pic)
    return pic


def get_pic_by_id(session: Session, pic_id: int) -> Picture | None:
    return session.scalar(
        select(Picture).where(Picture.id == pic_id)
    )


def update_pic(session: Session, pic: Picture, payload: PictureUpdate) -> Picture:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(pic, key, value)
    session.commit()
    session.refresh(pic)
    return pic


def delete_pic(session: Session, pic: Picture) -> None:
    session.delete(pic)
    session.commit()
