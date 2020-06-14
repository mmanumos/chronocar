import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
#Pending md5 for password

class User(BaseModel, Base):
    """ Class to define behavior and data for users """

    __tablename__ = 'User'
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    initial_mileage = Column(Integer, nullable=False)
    categories_sub = relationship("CategorySub", backref="User")

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)

    @property
    def categories_sub(self):
        """ Getter method to return all categories_sub associated to the user """
        from models.category_sub import CategorySub
        list_categories = models.storage.getobject(CategorySub, "User_id", self.id)
        return list_categories

    def login():
        """ login """
        pass
