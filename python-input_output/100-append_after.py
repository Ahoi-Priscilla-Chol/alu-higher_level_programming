#!/usr/bin/python3
"""Defines a function that inserts a line after lines matching a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a new line after each line containing search_string.

    Args:
        filename (str): The file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line to insert after matching lines.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
