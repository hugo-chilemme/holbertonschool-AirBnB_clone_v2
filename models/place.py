#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base

from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

mtm_amenity_place = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    ))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

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

    reviews = relationship('Review', backref='places', cascade='delete')
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False, back_populates="place_amenities")
    amenity_ids = []

    @property
    def reviews(self):
        """Retourne une liste des avis associés à un lieu."""
        from models import storage
        from models.review import Review
        my_list = []
        for review in storage.all(Review).values():
            if self.id == review.place_id:
                my_list.append(review)
        return my_list

    @property
    def amenities(self):
        """Retourne une liste des équipements disponibles dans un lieu."""
        from models import storage
        from models.amenity import Amenity
        my_list = []
        for amenity in storage.all(Amenity).values():
            if amenity.id in self.amenity_ids:
                my_list.append(amenity)
        return my_list

    @amenities.setter
    def amenities(self, value):
        """Définit les équipements disponibles dans un lieu."""
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
