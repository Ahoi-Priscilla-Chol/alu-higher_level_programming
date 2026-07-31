#!/usr/bin/python3
"""
This module contains the Base class.
"""


class Base:
    """
    Base class that manages the id attribute for all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
