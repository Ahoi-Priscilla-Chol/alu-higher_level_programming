#!/usr/bin/python3
"""Defines a list subclass with a sorted printing method."""


class MyList(list):
    """Represent a list, with an added method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
