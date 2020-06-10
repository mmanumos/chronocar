#all models(class) must be imported to verify if an object exists
import sqlalchemy
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

my_classes = ["User", "CategoryMain", "CategorySub"]

class DBStorage:
    """ Administration, manipulation and connection for database """
      
    __session = None #private attribute to manage session for database
    __engine =  None #private attribute that contains connection configuration

    def __init__ (self):
        """ Create the connection bridge with Database """
        MYSQL_USER = 'chrono_dev_user'
        MYSQL_PWD = 'chrono_dev_pwd'
        MYSQL_HOST = 'localhost'
        MYSQL_DB = 'chrono_dev_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

    def reload(self):
        """ Load all data in objects for sqlAlchemy metadata/map to be used by the session """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ remove session of a database """
        self.__session.remove()

    def insert(self, obj):
        """ Add the object to the map/metadata of the sqlalchemy orm """
        self.__session.add(obj)
        self.commit()

    def commit(self):
        """ Insert and update all changes for sqlalchemy map/metadata into database """
        self.__session.commit()

    def delete(self, obj=None):
        """ remove an object of a session and the Database  """
        if obj is not None:
            self.__session.delete(obj)
            self.commit()

    def getobject(self, cls=None, keyname=None, keyvalue=None, typereturn=None):
        """ Get objects/object depending class - This is essencial  """
        """ keyname - It can be any attribute of the class - No essencial """
        """ keyvalue - Value which it going to be compared against [keyname value]  """
        """ typereturn - Return the result by default in list format, but it can in dictionary format too  """

        dict_objs = {}
        if cls is not None:
            list_objs = self.__session.query(cls).all()
            if (keyname and keyvalue) is not None:
                for obj in list_objs:
                    if obj.__dict__[keyname] == int(keyvalue):
                        dict_objs[obj.__class__.__name__ + '.' + str(obj.id)] = obj
            else:
                for obj in list_objs:
                    dict_objs[obj.__class__.__name__ + '.' + str(obj.id)] = obj
            
            if typereturn == "Dict":
                return dict_objs
            else:
                list_objs = []
                for key, value in dict_objs.items():
                    list_objs.append(value.to_dict())
                return list_objs





    