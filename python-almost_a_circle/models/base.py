#!/usr/bin/python3
"""Defines the Base class, the parent of all other classes in this project."""
import json


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
