#!/usr/bin/python3
# 0-read_file
"""Implements a function that reads a text file"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
    filename (string): name of the file to read
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read())
    except:
        pass

read_file("text.txt")