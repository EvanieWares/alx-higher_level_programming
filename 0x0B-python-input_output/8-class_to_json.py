#!/usr/bin/python3
# 8-class_to_json
"""
Implements a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object

    Args:
    obj (object): an instance of a Class

    Return:
    The dictionary description with simple data structure
    """
    return obj.__dict__
