from __future__ import annotations

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from rubio_api.database import Base

class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))

    event: Mapped[Event] = relationship(back_populates="albums")

    pictures: Mapped[list[Picture]] = relationship(
        back_populates="album",
        cascade="all, delete-orphan"
    )

