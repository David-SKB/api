from typing import Union

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .schemas import CreateEventRequest, UpdateEventRequest
from sqlalchemy.orm import Session
from sqlalchemy import null, Boolean
from .database import get_db
from .models import Job, Event

app = FastAPI()

origins = [
    "https://4playnsg-calendar.duckdns.org",
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def read_root():
    return {"test": "successful"}

@app.post("/event")
def create(details: CreateEventRequest, db: Session = Depends(get_db)):
    to_create = Event(
        event_title=details.event_title,
        event_description=details.event_description,
        start_date=details.start_date,
        end_date=details.end_date,
        start_time=details.start_time,
        end_time=details.end_time,
        is_full_day_event=details.is_full_day_event,
        is_reccuring=details.is_reccuring,
        created_by=details.created_by,
        created_date=details.created_date,
        parent_event_id=details.parent_event_id,
        event_label = details.event_label
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

@app.get("/event")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Event).filter(Event.id == id).first()

@app.get("/events")
def get_all(db: Session = Depends(get_db)):
    return db.query(Event).all()

@app.delete("/event")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Event).filter(Event.id == id).delete()
    db.commit()
    return { "success": True }

@app.put("/event")
def put_by_id(id: int, event_title: str, db: Session = Depends(get_db)):
    #record = Session.ex
    event = db.query(Event).filter(Event.id == id).first()
    if (event == None):
        return { "success": False }
    event.event_title = event_title
    db.commit()

@app.put("/eventt")
def put_by_id(id: int, details: UpdateEventRequest, db: Session = Depends(get_db)):
    #record = Session.ex
    event = db.query(Event).filter(Event.id == id).first()
    if (event == None):
        return { "success": False }
    event.event_title=details.event_title
    event.event_description=details.event_description
    event.start_date=details.start_date
    event.end_date=details.end_date
    event.start_time=details.start_time
    event.end_time=details.end_time
    #event.is_full_day_event=Boolean(1)
    event.is_full_day_event = True if details.is_full_day_event else False
    #event.is_reccuring=details.is_reccuring,
    event.is_reccuring = True if details.is_reccuring else False
    event.created_by=details.created_by
    event.created_date=details.created_date
    event.parent_event_id=details.parent_event_id
    event.event_label = details.event_label
    db.commit()
    return { "success": True }