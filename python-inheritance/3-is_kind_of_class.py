#!/usr/bin/python3
"""Defines a function that checks inheritance-inclusive class membership."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of it.
    """
    return isinstance(obj, a_class)
