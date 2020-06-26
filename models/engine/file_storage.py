#!/usr/bin/python3
"""
Storage Class
"""
import models
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """return dictionary objects"""
        return self.__objects
    
    def new(self, obj):
        """storage to new with __objects __class__ __name__ and id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """serialize objectsto the JSON file"""
        with open(self.__file_path, encoding="UTF8", mode='w') as file:
            json.dump(slef.__objects, file)

    def reload(self):
        """convert Json to object"""
        try:
            with open(self.__file_path, encoding="UTF8", mode='r') as file:
                self.__objects = json.loads(file)
        except FileNotFoundError:
            pass