#!/usr/bin/python3
# 0-lookup
"""
This module implements a lookup function that returns
a list of available attributes and methods of an object
"""


def lookup(obj):
    return dir(obj)
