#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import os


if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            if (not kwargs.get("id", 0)):
                self.id = str(uuid.uuid4())

            if (kwargs.get("created_at", 0)):
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"])
            else:
                self.created_at = datetime.now()

            if (kwargs.get("updated_at", 0)):
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"])
            else:
                self.updated_at = self.created_at

            if (kwargs.get("__class__", 0)):
                del kwargs['__class__']
            self.__dict__.update(kwargs) 

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
