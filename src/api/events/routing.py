from fastapi import APIRouter
from .models import EventModel, EventsListSchema, EventCreateSchema, UpdateSchema

router = APIRouter()

# Get all


@router.get("/", response_model=EventsListSchema)
def read_events() -> EventsListSchema:
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


@router.get("/{event_id}", response_model=EventModel)
def get_items(event_id: int) -> EventModel:
    return {
        "id": event_id
    }

# Put


@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id: int, payload: UpdateSchema) -> EventModel:
    data = payload.model_dump()
    return {"id": event_id, **data}
