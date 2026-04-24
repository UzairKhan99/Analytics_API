from api.db.config import DATABASE_URL
from fastapi import APIRouter
from .schemas import EventSchema, EventsListSchema, EventCreateSchema, UpdateSchema
import os
router = APIRouter()

# Get all


@router.get("/", response_model=EventsListSchema)
def read_events() -> EventsListSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "results": [
            {"id": 3}, {"id": 2}, {"id": 4}
        ],
        "count": 3
    }

# Post


@router.post("/", response_model=EventCreateSchema)
def create_events(payload: EventCreateSchema) -> EventCreateSchema:
    return payload

# Get one


@router.get("/{event_id}", response_model=EventSchema)
def get_items(event_id: int) -> EventSchema:
    return {
        "id": event_id
    }

# Put


@router.put("/{event_id}", response_model=EventSchema)
def update_event(event_id: int, payload: UpdateSchema) -> EventSchema:
    print(payload.description)
    return {"id": event_id}
