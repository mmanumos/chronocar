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

    def __init__(self, id, mileage_limit, mileage_act, high, middle, low, created_at, updated_at, CategorySub_id):
        self.id = id
        self.mileage_limit = mileage_limit
        self.mileage_act = mileage_act
        self.high = high
        self.middle = middle
        self.low = low
        self.created_at = created_at
        self.updated_at = updated_at
        self.CategorySub_id = CategorySub_id