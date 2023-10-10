#!/usr/bin/python3
# 1-write_file
"""Implements a function that writes to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
    filename (string): the name of the file
    text (string): text to write to the file
    """
    with open(filename, 'w') as f:
        f.write(text)
