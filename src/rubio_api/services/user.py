from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.core.security import hash_password
from rubio_api.models.user import User
from rubio_api.api.v1.schemas.user import UserUpdate, UserCreate


def users(session: Session) -> Sequence[User]:
    return session.scalars(
        select(User)
    ).all()

def get_user_by_email(session: Session, email: str) -> User | None:
    return session.scalar(
        select(User).where(User.email == email)
    )

def add_user(session: Session, payload: UserCreate) -> User:
    user = User(
        email=payload.email,
        name=payload.name,
        hashed_password=hash_password(payload.password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user