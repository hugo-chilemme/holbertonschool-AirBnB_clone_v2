#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
