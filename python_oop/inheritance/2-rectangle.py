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
    def area(self):
        """Return the area of the rectangle.

        Returns:
            int: width multiplied by height.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle.

        Returns:
            str: the text [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    