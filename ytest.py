#!/usr/bin/python3
import models
from models.alert import Alert
from models.expense import Expense
from models.category_sub import CategorySub

#Myalert = Alert(1, 100, 0, 90, 65, 64, "2020-09-23", "2020-09-30", 2)
#models.storage.insert(Myalert)
#print(Myalert)

#Myexpense = Expense(1, 50000, "2020-09-23", "2020-09-23", 3500, 2)
#models.storage.insert(Myexpense)
#print(Myexpense)

mycs = models.storage.getobject(CategorySub, "id", 2)
print(mycs[0].expenses)
