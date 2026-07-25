#!/usr/bin/python3
"""Defines a function that returns a dict representation of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        A dictionary representation of obj's attributes.
    """
    return obj.__dict__
