#!/usr/bin/python3
"""Module that defines a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
