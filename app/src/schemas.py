from pydantic import BaseModel
from typing import Optional

class CreateJobRequest(BaseModel):
    title: str
    description: str

class CreateEventRequest(BaseModel):
    event_title: str
    event_description: str
    start_date: str
    end_date: str
    start_time: str
    end_time: str
    is_full_day_event: bool
    is_reccuring: bool
    created_by: str
    created_date: str
    parent_event_id: Optional[int]
    event_label: Optional[str]

class UpdateEventRequest(BaseModel):
    event_title: Optional[str]
    event_description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    is_full_day_event: bool
    is_reccuring: bool
    created_by: Optional[str]
    created_date: Optional[str]
    parent_event_id: Optional[int]
    event_label: Optional[str]