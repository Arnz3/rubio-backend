from pydantic import BaseModel, EmailStr, ConfigDict

class OrganizationCreate(BaseModel):
    name: str
    contact_email: EmailStr
    vat_number: str | None = None
    owner_id: int

class OrganizationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    contact_email: EmailStr
    vat_number: str | None
    owner_id: int

class OrganizationUpdate(BaseModel):
    name: str | None = None
    contact_email: EmailStr | None = None
    vat_number: str | None = None
    owner_id: int | None = None