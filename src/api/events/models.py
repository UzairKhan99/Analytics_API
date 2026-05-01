from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )
    __chunk_time_interval__ = "INTERNAL 1 day"
    __drop_after__ = "INTERNAL 3 months"


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ""


class EventsListSchema(SQLModel):
    results: List[EventModel]
    count: int


class UpdateSchema(SQLModel):
    description: str
