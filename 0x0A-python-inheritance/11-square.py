#!/usr/bin/python3
# 11-square
"""Implements a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class
    Inherits from Rectangle class
    """

    def __init__(self, size):
        """
        Initialization

        Args:
        size (int): size of the square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square

        Return:
        The area of the square
        """
        return self.__size * self.__size
