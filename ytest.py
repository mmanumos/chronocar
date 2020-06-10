#!/usr/bin/python3
import models
from models.alert import Alert
from models.expense import Expense
from models.category_sub import CategorySub
from models.user import User

#Myuser = User(name="User 5", last_name="Apellido 5", email="asdas@sdsd", password="password", initial_mileage=3000, created_at="2020-09-08", updated_at="2020-05-09")
#models.storage.insert(Myuser)
#print(Myuser.id)
#Mycs = CategorySub(id=5, name="Neumáticos", created_at="2020-09-08", updated_at="2020-05-09", CategoryMain_id=1, User_id=3)
#models.storage.insert(Mycs)
#print(Mycs)

#Myalert = Alert(901, 0, 90, 65, 64, "2020-09-23", "2020-09-30", 2)
#models.storage.insert(Myalert)
#models.storage.reload()
#print(Myalert.id)

#Myexpense = Expense(1, 50000, "2020-09-23", "2020-09-23", 3500, 2)
#models.storage.insert(Myexpense)
#print(Myexpense)

mycs = models.storage.getobject(User)
print(mycs[0])
