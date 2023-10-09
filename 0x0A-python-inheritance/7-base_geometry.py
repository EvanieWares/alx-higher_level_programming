#!/usr/bin/python3
# 7-base_geometry
"""Implements an BaseGeometry class"""


class BaseGeometry:
    """A class with a public instance methods"""

    def area(self):
        """
        Raises an exception with a message

        Raises:
        Exception: with a message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
