#!/usr/bin/python3
# 4-from_json_string
"""
Implements a function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
    my_str (string): The string

    Return:
    Object represented by a JSON string
    """
    import json
    return json.loads(my_str)
