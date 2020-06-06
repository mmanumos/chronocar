#all models(class) must be imported to verify if an object exists
import sqlalchemy
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

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

    def add(self, obj):
        """ Add the object to the map/metadata of the sqlalchemy orm """
        self.__session.add(obj)

    def commit(self):
        """ Insert and update all changes for sqlalchemy map/metadata into database """
        self.__session.commit()






    