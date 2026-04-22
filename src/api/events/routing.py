from fastapi import APIRouter
from typing import Union
from .schemas import EventSchema

router = APIRouter()


@router.get("/")
def get_items():
    return {
        "items": [1, 2, 3]
    }


@router.get("/{event_id}")
def get_items(event_id: int) -> EventSchema:
    return {
        "idd": event_id
    }
