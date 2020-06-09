from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("---- Reloaded objects ----")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("---- Create a new User 0 ----")
my_user0 = User()
my_user0.nickname = "ZeroUser"
my_user0.save()
print(my_user0)

print("---- Create a new User 1 ----")
my_user1 = User()
my_user1.nickname = "OneUser"
my_user1.save()
print(my_user1)
