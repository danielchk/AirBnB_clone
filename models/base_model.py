#!/usr/bin/python3
from uuid import uuid4                                                   #used to create a unique id every time
from datetime import date
from datetime import datetime

"""
Base class to models
"""

class BaseModel:
    """Base model instantiation"""
    
    def __init__(self, **kwargs):
        """
        Args:
        **kwargs: dictionary
        """
        dateform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())                                             #unique id representation to each BaseModel in a string type
        self.created_at = datetime.today()                                 #date when instance is created
        self.updated_at = datetime.today()                                 #date when instance is created and updated everytime we change an object
        if len(kwargs) ! = 0:
            for key, word in kwargs:
                if key == "created_at" 
        
        def save(self):
        """"Save command that update updated_at"""
        self.updated_at = datetime.today()