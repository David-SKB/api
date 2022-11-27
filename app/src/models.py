from sqlalchemy import Integer, String, Boolean, Date, Time, DateTime, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from .database import Base

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    event_title = Column(String, nullable=False)
    event_description = Column(String, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    is_full_day_event = Column(Boolean, nullable=False)
    is_reccuring = Column(Boolean, nullable=False)
    created_by = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False)
    parent_event_id = Column(Integer, ForeignKey("event.id"), nullable = True)
    event_label = Column(String, nullable = True)