#!/usr/bin/python3
"""
defines all common attributes/methods for other classes
"""

from uuid import uuid4

class BaseModel():
    def __init__(self):
        """initialize attributes"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
