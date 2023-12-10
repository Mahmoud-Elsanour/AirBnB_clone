#!/usr/bin/python3
"""
The User Class that inherits from  the BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A blueprint for a User object
    The public attributes will be used to manage the
    serialization and eserialization of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
