import models
from models.base_model import Base
from models.category_sub import CategorySub
from models.alert import Alert
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

class Expense(Base):
    """ Class that defines the behavior and data for expenses """

    __tablename__ = 'Expense'

    id = Column(Integer, nullable=False, primary_key=True)
    amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    mileage = Column(Integer, nullable=False)
    CategorySub_id = Column(Integer, ForeignKey(CategorySub.id), nullable=False)

    def __init__(self, id, amount, created_at, updated_at, mileage, CategorySub_id):
        """ Constructor """
        self.id = id
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at
        self.mileage = mileage
        self.CategorySub_id = CategorySub_id

    def UpdateAlertAct():
        """ Update all fields [mileage_act] according to the new current mileage """
        # AlertAct = ((NewMileage - CurrentMileage) + CurrentAlertAct)
        #
        #
        """ Call to class Alert method to identify alert priority in all alerts from preventive maintenance"""
        #Alert.IdentifyPriority(self.CategorySub_id)