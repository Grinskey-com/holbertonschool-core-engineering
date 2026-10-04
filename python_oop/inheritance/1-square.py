#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a sqaure, a rectangle with equal sides"""

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
    