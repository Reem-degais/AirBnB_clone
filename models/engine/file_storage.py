#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)]=obj

    def save(self):
        """serializes __objects to the JSON file"""
        objdict = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)


    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return


