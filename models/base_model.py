import models
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #The object is created to map all classes

class BaseModel:
    """  """

    id = Column(Integer, nullable=False, primary_key=True)  #Auto-increment should be default
    name = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """ Constructor builds the object in base of key(attribute) and value """
        for key, value in kwargs.items():
            setattr(self, key, value)    

    def to_dict(self):
        """ return the object like dictionary with some changes  """
        dict_obj = self.__dict__.copy()
        return dict_obj