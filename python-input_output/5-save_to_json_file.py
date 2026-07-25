#!/usr/bin/python3
"""Defines a function that saves an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object's JSON representation to a text file.

    Args:
        my_obj: The object to serialize and save.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
