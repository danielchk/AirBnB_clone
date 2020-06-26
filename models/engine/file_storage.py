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
        return FileStorage.__objects
    
    def new(self, obj):
        """storage to new with __objects __class__ __name__ and id"""
        obnew = obj.__class__.__name__
        obj = FileStorage.__objects["{}.{}".format(obnew.id)]
    
    def save(self):
        """serialize objectsto the JSON file"""
        with open(self.__class__.__file_path, "w+") as f:
            dictobjs = {}
            for key, value in self.__class__.__objects.items():
                dictobjs[key] = value.to_dict()
            f.write(json.dumps(dictobjs))
    
    def reload(self):
        """convert Json to object"""
        