#!/usr/bin/python3
import models
from models.user import User

myuser = User(1, "Camilo", "Mosquera", "2020-08-09", "2020-08-09", "assa@sdcsd", "password", 3000)
myuser.create()
