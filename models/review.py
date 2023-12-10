#!/usr/bin/python3
"""
A Definition of the state model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    A blueprint for the Review objects
    """
    user_id = ""
    place_id = ""
    text = ""
