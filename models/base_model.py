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

    def __init__(self, name, last_name, created_at, updated_at):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.created_at = created_at
        self.updated_at = updated_at

    def create(self):
        models.storage.add(self)
        models.storage.commit()



