#!/usr/bin/python3
"""This is the square class"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new instance of a square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
