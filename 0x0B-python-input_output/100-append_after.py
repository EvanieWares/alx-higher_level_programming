#!/usr/bin/python3
# 100-append_after
"""
Implements a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Implements a function that inserts a line of text to a file,
    after each line containing a specific string.

    Args:
    filename (string): name of the file
    search_string (string): the string to search for
    new_string (string): the string to insert
    """
    with open(filename) as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
