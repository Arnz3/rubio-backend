from pydantic import BaseModel, ConfigDict

class PictureRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    album_id: int
    full_url: str
    thumb_url: str


class PictureCreate(BaseModel):
    album_id: int


class PictureUpdate(BaseModel):
    album_id: int | None = None