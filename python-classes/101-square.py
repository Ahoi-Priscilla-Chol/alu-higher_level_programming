#!/usr/bin/python3
"""Defines a class Square that is printable."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: The size of the square.
            position: The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(i) is int for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #, using position."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation for printing the square."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
