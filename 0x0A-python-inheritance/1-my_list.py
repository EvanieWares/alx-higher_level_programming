#!/usr/bin/python3
# my_list
"""
Implements a class that inherits from list
"""


class MyList(list):
    """
    MyList class

    Inherits from list
    """

    def print_sorted(self):
        """
        Prints the list but sorted in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
