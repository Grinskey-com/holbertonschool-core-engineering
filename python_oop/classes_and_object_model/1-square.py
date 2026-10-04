#!/usr/bin/env python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the square (stored privately).
        """
        self.__size = size