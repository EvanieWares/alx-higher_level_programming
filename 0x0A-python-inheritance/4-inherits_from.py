#!/usr/bin/python3
# 4-inherits_from
"""
Implements a function that checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
    obj (object): the object to check
    a_class (class): the class

    Return:
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
