from datetime import datetime
from pydantic import BaseModel, ConfigDict

class AlbumRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    event_id: int


class AlbumCreate(BaseModel):
    name: str
    event_id: int


class AlbumUpdate(BaseModel):
    name: str | None = None
    event_id: int | None = None

