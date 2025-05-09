from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class TimestampMixin(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UuidMixin(SQLModel):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True, index=True)


class BaseMixin(UuidMixin, TimestampMixin):
    pass