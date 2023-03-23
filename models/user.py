#!/usr/bin/python3

"""This module defines a class User"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class User(BaseModel, Base):  
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    
    places = relationship('Place', backref='cities', cascade='delete')
=======
    reviews = relationship('Review', backref='user', cascade='all, delete-orphan')
>>>>>>> 4644e1e150dbf5feb17369e9749e732e05c92d04
