from pydantic import BaseModel
from typing import List, Optional


class EventSchema(BaseModel):
    id: int


class EventsListSchema(BaseModel):
    results: List[EventSchema]
    count: int


class EventCreateSchema(BaseModel):
    page: str
    page: Optional[str] = ""


class UpdateSchema(BaseModel):
    description: str
