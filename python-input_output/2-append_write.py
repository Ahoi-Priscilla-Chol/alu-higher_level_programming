#!/usr/bin/python3
"""Defines a function that appends a string to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return chars added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append.

    Returns:
        The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
