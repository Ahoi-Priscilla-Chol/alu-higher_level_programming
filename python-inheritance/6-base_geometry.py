#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represent a base geometry class."""

    def area(self):
        """Raise an Exception; area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
