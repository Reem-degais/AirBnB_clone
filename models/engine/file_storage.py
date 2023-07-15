#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    attributes:
     __file_path : The name of the file to save objects to.
     __objects : A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objdict = {key: obj.to_dict(
            ) for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj_id, obj_data in objdict.items():
                    cls_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(globals()[cls_name](**obj_data))
        except FileNotFoundError:
            return
