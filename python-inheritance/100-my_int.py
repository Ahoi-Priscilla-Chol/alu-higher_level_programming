#!/usr/bin/python3
"""Module that defines MyInt class"""


class MyInt(int):
    """A rebel integer class"""

    def __eq__(self, other):
        """Invert == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Invert != operator"""
        return int(self) == other
