#!/usr/bin/python3
"""
This module contains a function that adds two integers.

a and b must be numbers, otherwise a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Add two integers, casting floats to int first.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
