#!/usr/bin/python3
"""A module that serializes and deserializes json objects."""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ Abstract storage engin
    Attributes:
    __file_path: the name of the file to save json sting in
    __object: a dictionary of instaited objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all the object in file storage"""
        return self.__objects

    def new(self, obj):
        """creates a new object

        Args:
        obj: json object - strings
        """
        obj_name = obj.__class__.__name__
        value = "{}.{}".format(obj_name, obj.id)
        self.__objects[value] = obj

    def save(self):
        """serialize json file"""
        all_objects = self.__objects
        object_dict = {}

        for key in all_objects.keys():
            object_dict[key] = all_objects[key].to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """deserialize json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    object_dict = json.load(file)
                    for key, value in object_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)

                        self.__objects[key] = instance
                except Exception:
                    pass
