#!/usr/bin/env python3
"""Defines an abstract Shape class, two shapes, and a duck-typed function."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initialise a new Circle.

        Args:
            radius (int or float): the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialise a new Rectangle.

        Args:
            width (int or float): the width of the rectangle.
            height (int or float): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape.

    Works with any object that has area() and perimeter() methods.

    Args:
        shape: an object providing area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
