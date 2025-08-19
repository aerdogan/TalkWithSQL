from sqlalchemy import Boolean, Column, Integer, String
from modelbase import ModelBase

class Book(ModelBase):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher = Column(String)
    is_available = Column(Boolean, default=False)
