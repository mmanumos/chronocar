import json
import os.path
from ..base_model import BaseModel
from ..user import User


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}
    """ Private class attributes """

    def all(self):
        """ Public instance method that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Public instance method that sets in __objects
        the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Public instance method that serializes
        __objects to the JSON file """
        dict_temp = {}
        for key, value in FileStorage.__objects.items():
            dict_temp[key] = value.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(dict_temp))

    def reload(self):
        """ Public instance method that deserializes
        the JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dict_temp = json.loads(f.read())
                for key, value in dict_temp.items():
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
