from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.models.event import Event
from rubio_api.api.v1.schemas.event import EventCreate, EventUpdate

def list_events(session: Session) -> Sequence[Event]:
    return session.scalars(
        select(Event)
    ).all()


def add_event(session: Session, payload: EventCreate) -> Event:
    event = Event(**payload.model_dump())
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


def get_event_by_id(event_id: int, session: Session) -> Event | None:
    return session.scalar(
        select(Event).where(Event.id == event_id)
)


def update_event(event: Event, session: Session, payload: EventUpdate) -> Event: 
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(event, key, value)
    session.commit()
    session.refresh(event)
    return event


def delete_event(event: Event, session: Session) -> None:
    session.delete(event)
    session.commit()