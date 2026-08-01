#!/usr/bin/python3
"""Defines the Base class, the parent of all other classes in this project."""
import json
import os


class Base:
    """Base class that manages the id attribute for all future classes.

    This class serves as the base for the entire hierarchy of the project.
    It manages the `id` attribute of every future class and avoids
    duplicating the same code (`id` attribute management) in each class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance.
                If `id` is None, `__nb_objects` is incremented and used
                as the new instance's id. Otherwise, `id` is used as is.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of
        dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries, or None.

        Returns:
            str: `"[]"` if `list_dictionaries` is None or empty,
                otherwise the JSON string representation of it.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
