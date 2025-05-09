from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from app.database.models.mixins import BaseMixin


class UserDB(BaseMixin, table=True):
    __tablename__ = "users"

    identification_number: str = Field(index=True, max_length=20)
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    second_last_name: Optional[str] = None
    marital_status: str
    email: str
    phone_number: str

    is_politically_exposed: bool
    is_high_risk_business: bool
    has_us_residency: bool

    occupation_type: str  # options: SALARIED, SELF_EMPLOYED, INDEPENDENT_PROFESSIONAL, RETIRED
    employer_name: Optional[str] = None
    job_title: Optional[str] = None
    employment_start_date: Optional[datetime] = None
    monthly_gross_income: float

    home_address: str
    work_address: str

    beneficiaries: List["BeneficiaryDB"] = Relationship(back_populates="user")


class BeneficiaryDB(BaseMixin, table=True):
    __tablename__ = "beneficiaries"

    identification_number: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    second_last_name: Optional[str] = None
    relationship: str  # options: MOTHER, FATHER, CHILD, SIBLING, SPOUSE, COMMON_LAW_PARTNER, OTHER
    phone_number: str
    email: str
    percentage: float
    wants_to_add_another: bool

    user_id: UUID = Field(foreign_key="users.uuid")
    user: Optional[UserDB] = Relationship(back_populates="beneficiaries")
