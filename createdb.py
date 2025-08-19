import models
from sqlalchemy import create_engine
from modelbase import ModelBase

engine = create_engine("sqlite:///ornek.db")
ModelBase.metadata.create_all(bind=engine)
