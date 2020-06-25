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
        """dictionary objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        obnew = obj.__class__.__name__
        obj = FileStorage.__objects["{}.{}".format(obnew.id)]