from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.orm import Session
from rubio_api.database import get_session

from rubio_api.api.v1.schemas.organization import OrganizationCreate, OrganizationRead, OrganizationUpdate
from rubio_api.services import organization as org_service

router = APIRouter(prefix="/organization", tags=["organization"])
sessionDep = Annotated[Session, Depends(get_session)]


@router.get("/", response_model=list[OrganizationRead])
async def get_organizations(session:sessionDep):
    return org_service.list_organizations(session)


@router.get("/{org_id}", response_model=OrganizationRead)
async def get_org_by_id(org_id: int, session:sessionDep):
    org = org_service.get_organization_by_id(session, org_id)
    if org is None:
        raise HTTPException(status_code=404, detail="Organization not Found")
    return org


@router.post("/", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
async def create_organization(payload: OrganizationCreate, session:sessionDep):
    if org_service.get_organization_by_email(session, payload.contact_email):
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail="Organization with this contact_email already exists"
        )
    return org_service.add_organization(session, payload)


@router.put("/{org_id}", response_model=OrganizationRead)    
async def update_organization(org_id: int, payload: OrganizationUpdate, session: sessionDep) -> OrganizationRead:
    org = org_service.get_organization_by_id(session, org_id)
    if org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )
    return org_service.update_organization(session, org, payload)


@router.delete("/{org_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_organization(org_id: int, session: sessionDep):
    org = org_service.get_organization_by_id(session, org_id)
    if org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )
    org_service.remove_organization(session, org)