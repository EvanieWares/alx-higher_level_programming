#!/usr/bin/python3
# 101-add_attribute
"""Implements a function that add attributes to a class"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds attributes to an object if it's possible

    Args:
    obj (object): the object
    attr_name: name of the attribute to be added
    attr_value: value of the attribute

    Raises:
    TypeError: if a new attribute can't be added
    """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attr_name in obj.__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
