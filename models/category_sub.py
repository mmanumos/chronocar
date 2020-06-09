import models
from models.base_model import BaseModel, Base
from models.category_main import CategoryMain
from models.user import User
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class CategorySub(BaseModel, Base):
    """ class tha defines behavior and data for subcategories  """
    __tablename__ = 'CategorySub'
    CategoryMain_id = Column(Integer,ForeignKey(CategoryMain.id), nullable=False)
    User_id = Column(Integer, ForeignKey(User.id), nullable=False)
    alerts = relationship("Alert", backref="CategorySub")
    expenses = relationship("Expense", backref="CategorySub")

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)

    @property
    def alerts(self):
        """ Getter method to return all alerts associated to the CategorySub """
        from models.alert import Alert
        list_alert = models.storage.getobject(Alert, "CategorySub_id", self.id)
        return list_alert

    @property
    def expenses(self):
        """ Getter method to return all expenses associated to the CategorySub """
        from models.expense import Expense
        list_expense = models.storage.getobject(Expense, "CategorySub_id", self.id)
        return list_expense