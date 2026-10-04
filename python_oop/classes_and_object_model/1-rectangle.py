#!/usr/bin/env python3
"""Defines a rectangle class with validated witdth and length."""


class Rectangle:
    """represents a rectangle."""

    def __init__(self, width=0, height=0):
        """intinalise a new rectangle

        args:
            width (int): the width of the rectangle.
            height (int): the height of the rectange.
        """
        self.width = width
        self.height = height

    @property
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): the new width.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width musy be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self,vaue):
        """Set the height of the rectangle.

        Args:
            value (int): the new height.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value 
        