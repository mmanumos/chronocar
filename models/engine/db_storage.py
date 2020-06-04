#all models(class) must be imported to verify if an object exists
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scopped_session, sessionmaker


class DBStorage:
    """ Administration, manipulation and connection for database """

    __session = None
    __engine =  None

    def __init__ (self):
        """ Create the connection bridge with Database """
        MYSQL_USER = 'chrono_dev_user'
        MYSQL_PWD = 'chrono_dev_pwd'
        MYSQL_HOST = 'localhost' 
        MYSQL_DB = 'chrono_dev_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB))

    def reload(self):
        """ Load all data in objects for sqlAlchemy metadata to be used by the session """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scopped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ remove session of a database """
        self.__session.remove()






    