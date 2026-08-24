"""
Database connection and session handling.
Provides a database session to each request via ``Depends(get_db)``.
``Base`` is defined here so that all models share the same declarative base.
"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from rubio_api.config import settings

Base = declarative_base()

engine = create_async_engine(settings.database_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
