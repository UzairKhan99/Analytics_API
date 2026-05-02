from typing import ClassVar, List, Optional

import sqlmodel
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class EventModel(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"autoincrement": True},
    )
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        primary_key=True,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )
    __time_column__: ClassVar[str] = "created_at"
    __chunk_time_interval__: ClassVar[str] = "INTERVAL 1 day"
    __drop_after__: ClassVar[str] = "INTERVAL 3 months"


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = ""


class EventsListSchema(SQLModel):
    results: List[EventModel]
    count: int


class EventBucketSchema(SQLModel):
    bucket: datetime
    page: Optional[str] = ""
    count: int


class UpdateSchema(SQLModel):
    description: str
