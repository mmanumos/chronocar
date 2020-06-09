import models
from models.base_model import BaseModel, Base
from models.category_main import CategoryMain
from models.user import User
from sqlalchemy import Column, String, Integer, ForeignKey 

class CategorySub(BaseModel, Base):
    """ class tha defines behavior and data for subcategories  """
    __tablename__ = 'CategorySub'
    CategoryMain_id = Column(Integer,ForeignKey(CategoryMain.id), nullable=False)
    User_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)