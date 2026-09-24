from __future__ import annotations

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rubio_api.database import Base

class Picture(Base):
    __tablename__ = "pictures"

    id: Mapped[int] = mapped_column(primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))
    full_url: Mapped[str] = mapped_column(unique=True)
    thumb_url: Mapped[str | None] = mapped_column(unique=True)

    album: Mapped[Album] = relationship(back_populates="pictures")