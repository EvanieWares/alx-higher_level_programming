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
    import json
    with open(file=filename, mode='w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
