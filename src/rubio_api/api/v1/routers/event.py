
from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session
from rubio_api.database import get_session

from rubio_api.api.v1.schemas.event import EventCreate, EventRead, EventUpdate
from rubio_api.services import event as org_event


router = APIRouter(prefix="/event", tags=["event"])
sessionDep = Annotated[Session, Depends(get_session)]

@router.get("/", response_model=list[EventRead])
async def get_events(session:sessionDep):
    return org_event.list_events(session)


@router.get("/{event_id}", response_model=EventRead)
async def get_event_by_id(event_id: int, session:sessionDep):
    event = org_event.get_event_by_id(event_id, session)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("/", response_model=EventRead, status_code=status.HTTP_201_CREATED)
async def create_event(payload: EventCreate, session:sessionDep):
    return org_event.add_event(session, payload)


