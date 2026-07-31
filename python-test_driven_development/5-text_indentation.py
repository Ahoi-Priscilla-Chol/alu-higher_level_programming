#!/usr/bin/python3
"""
This module contains a function that prints text with indentation.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = [line.strip() for line in result.split("\n")]
    print("\n".join(lines).strip("\n"), end="")
