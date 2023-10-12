#!/usr/bin/python3
# 2-append_write
"""Implements a function that append a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added

    Args:
    filename (string): the name of the file
    text (string): text to write to the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
