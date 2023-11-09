#!/usr/bin/python3
"""
A class with no class or object attribute
"""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ["first_name"]
