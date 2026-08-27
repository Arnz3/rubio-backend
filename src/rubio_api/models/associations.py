from sqlalchemy import Column, ForeignKey, Integer, Table

from rubio_api.database import Base

user_org = Table(
    "user_org",
    Base.metadata,
    Column(
        "organization_id",
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
)