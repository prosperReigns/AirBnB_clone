#!/usr/bin/python3
""" a module for a class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the base of a model"""

    instance_count = 0

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print a string representaion of Base model"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update time upon saving"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """convert instance to object (dictionary)"""

        base_dict = self.__dict__.copy()
        base_dict["__class__"] = __class__.__name__
        base_dict["id"] = self.id
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()

        return base_dict
