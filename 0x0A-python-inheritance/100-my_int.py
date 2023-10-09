#!/usr/bin/python3
# 100-my_int
"""Implements MyInt class"""


class MyInt(int):
    """
    MyInt class
    Inherits from int class
    """

    def __eq__(self, value):
        """
        Checks if values are equal

        Return:
        True if self==value, otherwise False

        Notes:
        This method will be altered to do just the opposite

        Return:
        True if self!=value, otherwise False
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        Checks if values are not equal

        Return:
        True if self!=value, otherwise False

        Notes:
        This method will be altered to do just the opposite

        Return:
        True if self==value, otherwise False
        """
        return super().__eq__(value)
