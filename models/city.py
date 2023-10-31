#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.place import Place


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    @property
    def places(self):
        """
        Getter attribute to return the list of Place instances with city_id
        equal to the current City.id
        """
        places_list = []
        all_places = storage.all(Place)
        for place in all_places.values():
            if place.city_id == self.id:
                places_list.append(place)
        return places_list

    def get(self, id):
        """
        Retrieve an object by ID.
        """
        return storage.get(City, id)

    def count(self):
        """
        Count the number of City objects.
        """
        return len(storage.all(City))