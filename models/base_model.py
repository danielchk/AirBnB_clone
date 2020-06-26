#!/usr/bin/python3
import models
from uuid import uuid4                                                   #used to create a unique id every time
from datetime import datetime

"""
Base class to models
"""

class BaseModel:
    """
    Base model instantiation
    """
    
    def __init__(self, *args, **kwargs):
        """
        Args:
        **kwargs: dictionary
        """
        dateform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())                                             #unique id representation to each BaseModel in a string type
        self.created_at = datetime.today()                              #date when instance is created
        self.updated_at = datetime.today()                                 #date when instance is created and updated everytime we change an object

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":             #gonna create a datetime object
                        value = datetime.strptime(value, dateform)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Save command that update updated_at
        """
        self.updated_at = datetime.today()                                 #date when instance is created and updated everytime we change an object
        models.storage.save()
               
    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict