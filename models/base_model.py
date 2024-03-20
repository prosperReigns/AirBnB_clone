#!/usr/bin/python3
""" a module for a class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the base of a model"""

    def __init__(self, *args, **kwargs):
        """instantiate the instance of a class

        Args:
            name: the name of the model
            number: model number
            id: the id of the model
            created_at: time model was created
            updated_at: time model was modified
        """
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            created_at_dict = kwargs['created_at']
            kwargs['created_at'] = \
                datetime.strptime(created_at_dict, time_format)
            updated_at_dict = kwargs['updated_at']
            kwargs['updated_at'] = \
                datetime.strptime(updated_at_dict, time_format)

            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
            else:
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
