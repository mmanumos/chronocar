#!/usr/bin/python3
import models
from models.user import User

myuser = User(1, "Manuel", "Mosquera", "2020-08-09", "2020-08-09", "asas@asdas", "passw", 3000)
myuser.create()
