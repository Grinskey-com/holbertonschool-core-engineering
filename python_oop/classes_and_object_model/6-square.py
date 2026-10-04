#!/usr/bin/env python3
"""Defines a Square class with size, position and a string form."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            position (tuple): the offset used when printing.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): the new size.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """tuple: the (x, y) offset used when printing."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): two non-negative integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: the size squared.
        """
        return self.__size ** 2

    def __str__(self):
        """Return the square drawn with # and offset by position.

        Returns:
            str: the drawing, without a trailing newline.
        """
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join([row] * self.__size)

    def my_print(self):
        """Print the square with # (an empty line if size is 0)."""
        print(str(self))
