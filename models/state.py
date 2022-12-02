#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    if models.storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all")
    else:
        name = ""

        @property
        def cities(self):
            """getter for cities that return
            a list of city instance equale to
            curent state id
            """
            list_city = []
            all_inst_c = models.storage.all(City)
            for value in all_inst_c.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return (list_city)
