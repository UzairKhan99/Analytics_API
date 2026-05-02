from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import cast, func
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlmodel import Session, select

from api.db.session import get_session
from .models import (
    EventBucketSchema,
    EventModel,
    EventsListSchema,
    EventCreateSchema,
    UpdateSchema,
    get_utc_now,
)

router = APIRouter()


@router.get("/analytics", response_model=List[EventBucketSchema])
def read_events_analytics(
    duration: str = Query(default="1 day"),
    pages: Optional[List[str]] = Query(default=None),
    session: Session = Depends(get_session)
):
    bucket = func.time_bucket(
        cast(duration, INTERVAL),
        EventModel.created_at,
    ).label("bucket")
    query = (
        select(
            bucket,
            EventModel.page.label("page"),
            func.count(EventModel.id).label("count"),
        )
        .group_by(
            bucket,
            EventModel.page,
        )
        .order_by(
            bucket,
            EventModel.page,
        )
    )

    if pages:
        query = query.where(EventModel.page.in_(pages))

    results = session.exec(query).all()
    return [
        {"bucket": bucket, "page": page, "count": count}
        for bucket, page, count in results
    ]


@router.get("/", response_model=EventsListSchema)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
    results = session.exec(query).all()
    return {
        "results": results,
        "count": len(results)
    }


@router.post("/", response_model=EventModel)
def create_events(payload: EventCreateSchema, session: Session = Depends(get_session)):
    data = payload.model_dump()
    obj = EventModel(**data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return result


@router.put("/{event_id}", response_model=EventModel)
def update_event(event_id: int,
                 payload: UpdateSchema,
                 session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    event = session.exec(query).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    data = payload.model_dump()
    for key, value in data.items():
        setattr(event, key, value)
    event.updated_at = get_utc_now()
    session.add(event)
    session.commit()
    session.refresh(event)
    return event
