#!/usr/bin/python3
# 3-is_kind_of_class
"""
Implements a function that checks if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class

    Args:
    obj (object): the object to check
    a_class (class): the class

    Return:
    True if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
