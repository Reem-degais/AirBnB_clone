#!/usr/bin/python3
"""Defines City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
       represent City
       attributes:
        state_id : The state id.
        name : The name of the city.
    """
    state_id = ""
    name = ""
