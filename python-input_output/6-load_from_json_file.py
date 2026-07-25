#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        The Python object represented by the file's JSON content.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
