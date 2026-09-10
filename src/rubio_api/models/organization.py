from __future__ import annotations

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rubio_api.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contact_email: Mapped[str] = mapped_column(String(255), unique=True)
    vat_number: Mapped[str | None] = mapped_column(unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    ### SOFT RELATIONS
    # many-to-one: the owner
    owner: Mapped[User] = relationship(back_populates="owned_organizations")

    # one-to-many: events of organisation
    events: Mapped[list[Event]] = relationship(
        back_populates="organizer",
        cascade="all, delete-orphan"
    )

