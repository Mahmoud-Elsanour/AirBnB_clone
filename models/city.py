#!/usr/bin/python3
"""
A Definition of the state model
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Blueprint for City objects
    """
    state_id = ""
    name = ""
