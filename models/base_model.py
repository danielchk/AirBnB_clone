#!/usr/bin/python3
import models
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
        *args:
        **kwargs: dictionary
        """
        self.id = str(uuid4())                 #unique id representation to each BaseModel in a string type
        self.created_at=
    