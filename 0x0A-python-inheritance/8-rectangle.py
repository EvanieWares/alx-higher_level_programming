#!/usr/bin/python3
# 8-rectangle.py
"""Implements a class that inherits from another class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        """
        Initialization

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
