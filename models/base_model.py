import models
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

""" The object is created to map all classes """
Base = declarative_base()

class BaseModel:
    
    id = Column(Integer, nullable=False, primary_key=True)  #Auto-increment should be default
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """  """
        for key, value in kwargs.items():
            setattr(self, key, value)    
        
    def create(self):
        """  """
        models.storage.add(self)
        models.storage.commit()
