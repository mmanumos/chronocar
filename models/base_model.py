from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """" Constructor with public instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Method that define print """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ Method that updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method that returns a dictionary containing all keys/values of
        __dict__ of the instance """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return(my_dict)
