from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from rubio_api.models.organization import Organization
from rubio_api.api.v1.schemas.organization import OrganizationCreate, OrganizationUpdate


def list_organizations(session: Session) -> Sequence[Organization]:
    return session.scalars(
        select(Organization)
    ).all()


def get_organization_by_email(session: Session, email: str) -> Organization | None:
    return session.scalar(
        select(Organization).where(Organization.contact_email == email)
    )

def get_organization_by_id(session: Session, id: int) -> Organization | None:
    return session.scalar(
        select(Organization).where(Organization.id == id)
    )

def add_organization(session: Session, payload: OrganizationCreate) -> Organization:
    org = Organization(**payload.model_dump())
    session.add(org)
    session.commit()
    session.refresh(org)
    return org


def update_organization(session: Session, org: Organization, payload: OrganizationUpdate) -> Organization:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(org, field, value)
    session.commit()
    session.refresh(org)
    return org


def remove_organization(session: Session, org: Organization) -> None:
    session.delete(org)
    session.commit()
