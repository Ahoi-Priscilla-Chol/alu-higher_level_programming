#!/usr/bin/python3
"""Defines a function that checks strict inheritance from a class."""


def inherits_from(obj, a_class):
    """Check if an object's class inherited from the given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherited from
        a_class, but not a_class itself. Otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
