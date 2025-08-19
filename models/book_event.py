from enum import Enum
from sqlalchemy import Column, Enum as SQLEnum, Integer, DateTime
from modelbase import ModelBase

class GivenEnum(str, Enum):
    ToUser = "User"
    ToLibrary = "Library"

class Book_Event(ModelBase):
    __tablename__ = "book_events"
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime)
    book_id = Column(Integer)
    user_id = Column(Integer)
    given = Column(SQLEnum(GivenEnum), default=GivenEnum.ToLibrary)
