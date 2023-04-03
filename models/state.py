#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        from models import storage
        my_list = []
        for i in storage.all(State).values():
            my_list.append(i)
        return my_list
