from __future__ import annotations

from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rubio_api.database import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    organizer_id: Mapped[int] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"))
    start: Mapped[datetime | None]
    end: Mapped[datetime | None]

    organizer: Mapped[Organization] = relationship(back_populates="events")
    
