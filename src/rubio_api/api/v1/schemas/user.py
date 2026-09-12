from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    name: str

class UserUpdate(BaseModel):
    email: EmailStr | None
    name: str | None
    password: str | None
