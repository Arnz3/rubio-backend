from sqlalchemy import String, Column, Integer

from rubio_api.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String, nullable=False)
    contact_email = Column(String, unique=True, nullable=False)
    vat_number = Column(String, nullable=True)
    owner_id = Column(Integer, nullable=False)


