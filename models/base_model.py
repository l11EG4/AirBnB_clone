#!/usr/bin/python3
"""Defines BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base class that defines common attributes and methods for others classes."""

    def __init__(self, *args, **kwargs):
        """ Initialize new BaseModel.

            Args:
                *args : Unused.
                **kwargs : key/value pairs.
        """
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for c, u in kwargs.items():
                if c == "created_at" or c == "updated_at":
                    self.__dict__[c] = datetime.strptime(u, tf)
                else:
                    self.__dict__[c] = u
        else:
            models.storage.new(self)

    def save(self):
        """
        Update public instace attribute with updated_at with the current datetime.
        and save the instance to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary contains all keys/values of __dict__ of instance.
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = class_name
        return obj_dict

    def __str__(self):
        """
        Returns a string in format :[<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
