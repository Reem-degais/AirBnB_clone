#!/usr/bin/python3
from models.engine.file_storage import BaseModel
"""Defines the State class."""


class State(BaseModel):
    """represent a state.
       attributes:
        name : The name of the state.
    """
    name = ""
