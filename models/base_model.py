#!/usr/bin/python3
"""
Module for the Base class
Contains the Base class for the AirBnB clone console project
It will be the base class for all other classes
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Class for the base model for all objects"""

    def __init__(self, *args, **kwargs):
        """
        Initialization of a Base instance.

        Args:
            - *args: list of arguments without a key
            - **kwargs: dict of key-value arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return a human-readable string representation of the instance
        """
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current date and time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
