#!/usr/bin/python3
import models
from uuid import uuid4                                                   #used to create a unique id every time
from datetime import date
from datetime import datetime

"""
Base class to models
"""

class BaseModel:
    """Base model instantiation"""
    
    def __init__(self, *args, **kwargs):
        """
        Args:
        **kwargs: dictionary
        """
        dateform = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.today()                                 #date when instance is created and updated everytime we change an object
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":             #gonna create a datetime object
                    date = datetime.strptime(value, dateform)
        else:
            self.id = str(uuid4())                                             #unique id representation to each BaseModel in a string type
            self.created_at = datetime.today()                                 #date when instance is created
            self.

        def save(self):
        """"Save command that update updated_at"""
        self.updated_at = datetime.today()
        