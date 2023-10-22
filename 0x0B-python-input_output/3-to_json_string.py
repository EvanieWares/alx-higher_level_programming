#!/usr/bin/python3
# 3-to_json_string
"""
Implements a function that returns a JSON representation
of an object (string)
"""


def to_json_string(my_obj):
    """
    Returns a JSON representation of an object

    Args:
    my_obj (object): string

    Return:
    JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
