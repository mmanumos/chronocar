import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
#Pending md5 for password

class User(BaseModel, Base):
    __tablename__ = 'User'
    email = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    initial_mileage = Column(Integer, nullable=False)

    def __init__(self, name, last_name, created_at, updated_at, email, password, initial_mileage):
        BaseModel.__init__(self, name, last_name, created_at, updated_at)
        self.email = email
        self.password = password
        self.initial_mileage = initial_mileage

