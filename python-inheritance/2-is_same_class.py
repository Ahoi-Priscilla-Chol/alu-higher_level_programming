#!/usr/bin/python3
"""Defines a function that checks for an exact class match."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
