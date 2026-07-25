#!/usr/bin/python3
"""Defines a function that returns a JSON string representation."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to serialize.

    Returns:
        A JSON-formatted string representing my_obj.
    """
    return json.dumps(my_obj)
