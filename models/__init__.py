from models.engine.db_storage import DBStorage

""" An instance of DBStorage common for all models """
storage = DBStorage()
storage.reload()
