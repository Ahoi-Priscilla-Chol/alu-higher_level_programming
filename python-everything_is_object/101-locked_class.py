#!/usr/bin/python3
"""Defines a class that restricts dynamic attribute creation."""


class LockedClass:
    """A class that only allows a first_name instance attribute."""

    __slots__ = ["first_name"]
