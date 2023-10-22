#!/usr/bin/python3
# 5-save_to_json_file
"""
Implements a function that creates an Object from a "JSON file"
"""


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"

    Args:
    filename (string): Name of the file to read from

    Return:
    Object
    """
    from_json_string = __import__("4-from_json_string").from_json_string
    with open(file=filename, encoding="utf-8") as file:
        return from_json_string(file.read())
