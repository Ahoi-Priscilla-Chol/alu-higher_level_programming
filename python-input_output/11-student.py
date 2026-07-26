#!/usr/bin/python3
"""Defines a Student class with save/reload via dictionary."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.
                If not a list, all attributes are included.

        Returns:
            A dictionary of the student's attributes, filtered by attrs
            if it is a list of strings.
        """
        if type(attrs) is list:
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
