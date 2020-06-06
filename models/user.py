import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
#Pending md5 for password

class User(BaseModel, Base):
    """ Class to define behavior and data for users """

    __tablename__ = 'User'
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    initial_mileage = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)

    def login():
        """ login """
        pass
