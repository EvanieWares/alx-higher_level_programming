#!/usr/bin/python3
# 0-lookup
"""
This module implements a lookup function that returns
a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns a list of available attributes and methods of an object

    Args:
    obj (object): object

    Return:
    a list of available attributes and methods of an object
    """
    return dir(obj)
