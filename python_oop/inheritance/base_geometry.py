#!/usr/bin/env python3
"""Defines a BaseGeometry class with area and integer validation."""

class BaseGeometry:
    """Base class for geometric shapes."""
    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be and integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        