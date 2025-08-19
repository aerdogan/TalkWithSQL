from sqlalchemy import Column, Integer, String
from modelbase import ModelBase

class User(ModelBase):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    total_rent_book_count = Column(Integer, default=0)
    current_rent_book_count = Column(Integer, default=0)
