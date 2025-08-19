from enum import Enum
from sqlalchemy import Column, Enum as String, Integer, DateTime
from modelbase import ModelBase

class Book_Event(ModelBase):
    __tablename__ = "book_events"
    event_id = Column(Integer, primary_key=True)
    event_date = Column(DateTime)
    event_type = Column(String)
    book_id = Column(Integer)
    user_id = Column(Integer)
