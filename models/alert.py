import models
from models.base_model import Base
from models.category_sub import CategorySub
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

class Alert(Base):
    """ Class that defines the behavior and data for alerts  """

    __tablename__ = 'Alert'
    id = Column(Integer, nullable=False, primary_key=True)
    mileage_limit = Column(Integer, nullable=False)
    mileage_act = Column(Integer, nullable=False)
    high = Column(Integer, nullable=False)
    middle = Column(Integer, nullable=False)
    low = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    CategorySub_id = Column(Integer, ForeignKey(CategorySub.id), nullable=False)

    def __init__(self, **kwargs):
        """ Constructor builds the object in base of key(attribute) and value """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """ return the object like dictionary with some changes  """
        dict_obj = self.__dict__.copy()
        if dict_obj['_sa_instance_state']:
            del dict_obj['_sa_instance_state']
        return dict_obj