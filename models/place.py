#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
<<<<<<< HEAD
from models.base_model import Base

from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
=======
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
>>>>>>> b1468f0d64ed2be0d074a52fbb8a3f8015332d36

class Place(BaseModel, Base):
    """places"""
    
    __tablename__ = "places"
    
<<<<<<< HEAD
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
         
    amenity_ids = []
=======
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    if models.storage_type == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        @property
        def reviews(self):
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list
>>>>>>> b1468f0d64ed2be0d074a52fbb8a3f8015332d36
