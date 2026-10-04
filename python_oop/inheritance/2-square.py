#!/usr/bin/env python3
"""Defines a Square class with its own string representation."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square.

        Returns:
            int: size multiplied by size.
        """
        return self.__size * self.__size

    def __str__(self):
        """Return the description of the square.

        Returns:
            str: the text [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
