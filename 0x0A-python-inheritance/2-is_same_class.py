#!/usr/bin/python3
# 2-is_same_class
"""
Implements a function that checks if the object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class

    Args:
    obj (object): the object to check
    a_class (class): the class

    Return:
    True if the object is exactly an instance of the specified class
    otherwise False
    """
    return type(obj) is a_class
