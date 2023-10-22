#!/usr/bin/python3
# 10-student
"""Implements a class Student"""


class Student:
    """
    A class Student that defines a student by:
            - first_name
            - last_name
            - age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student class

        Args:
        first_name (string): The first name of the student
        last_name (string): The last name of the student
        age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
        attrs (list): a list of attributes

        Return:
        A dictionary representation of a Student instance
        """
        d = self.__dict__
        if attrs is not None:
            st_dict = {key: d[key] for key in attrs if key in d}
            return st_dict
        return d
