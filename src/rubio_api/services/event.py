from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.models.event import Event
from rubio_api.api.v1.schemas.event import EventCreate, EventRead

def list_events(session: Session) -> Sequence[Event]:
    return session.scalars(
        select(Event)
    ).all()

def add_event(session: Session, payload: EventCreate) -> EventRead:
    pass