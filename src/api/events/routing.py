from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from .models import EventModel, EventsListSchema, EventCreateSchema, UpdateSchema
from .session import get_session

router = APIRouter()


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
    for keys, value in data.item():
        setattr(event, keys, value)
    obj.updated_at = get__utc_now()
    session.add(event)
    session.commit()
    session.refresh(event)
    return event
