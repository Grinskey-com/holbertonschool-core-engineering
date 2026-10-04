#!/usr/bin/env python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated private dimensions."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height