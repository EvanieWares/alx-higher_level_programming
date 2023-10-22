#!/usr/bin/python3
# 5-save_to_json_file
"""
Implements a function that writes an Object to a text file,
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file using a JSON representation

    Args:
    my_obj (object): The object to write to file
    filename (string): Name of the file
    """
    to_json_string = __import__("3-to_json_string").to_json_string
    with open(file=filename, mode='w', encoding="utf-8") as file:
        file.write(to_json_string(my_obj))
