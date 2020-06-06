import models
from models.base_model import BaseModel, Base

class CategoryMain(BaseModel, Base):
    """ CategoryMain is the father of CategorySub in data """
    __tablename__ = 'CategoryMain'

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)