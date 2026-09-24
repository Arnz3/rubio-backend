from datetime import datetime
from pydantic import BaseModel, ConfigDict

class EventCreate(BaseModel):
    name: str
    organizer_id: int
    start: datetime | None = None
    end: datetime | None = None

class EventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    organizer_id: int
    start: datetime | None
    end: datetime | None

class EventUpdate(BaseModel):
    name: str | None = None
    organizer_id: int | None = None
    start: datetime | None = None
    end: datetime | None = None