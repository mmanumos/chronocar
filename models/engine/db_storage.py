#all models(class) must be imported to verify if an object exists
import sqlalchemy
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

class DBStorage:
    """ Administration, manipulation and connection for database """

    __session = None
    __engine =  None

    def __init__ (self):
        """ Create the connection bridge with Database """
        MYSQL_USER = 'chrono_dev_user'
        MYSQL_PWD = 'chrono_dev_pwd'
        MYSQL_DB = 'chrono_dev_db'

        with SSHTunnelForwarder(
            ('54.209.158.161', 22),
            ssh_username='ubuntu',
            ssh_pkey='~/.ssh/holberton',
            remote_bind_address=('127.0.0.1', 3306)
        )  as server:
            server.start()  # start ssh sever
            local_port = str(server.local_bind_port)
            self.__engine= create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(MYSQL_USER,
                                                                                    MYSQL_PWD,
                                                                                    '127.0.0.1',
                                                                                    local_port,
                                                                                    MYSQL_DB),
                               pool_recycle=1)

    def reload(self):
        """ Load all data in objects for sqlAlchemy metadata to be used by the session """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ remove session of a database """
        self.__session.remove()

    def add(self, obj):
        """ Add the object to the map of the sqlalchemy orm """
        self.__session.add(obj)

    def commit(self):
        self.__session.commit()






    