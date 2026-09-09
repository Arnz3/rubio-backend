"""
Database connection and session handling.
``Base`` is defined here so that all models share the same declarative base.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, sessionmaker
from rubio_api.config import settings

class Base(DeclarativeBase):
    pass

engine = create_engine(settings.database_url)
session_maker = sessionmaker(engine, expire_on_commit=False)

def get_session() -> Generator[Session]:
    with session_maker() as session:
        yield session
