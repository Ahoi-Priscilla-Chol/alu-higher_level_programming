#!/usr/bin/python3
"""Defines a function that writes a string to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return chars written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
