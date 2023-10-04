#!/usr/bin/python3
"""
A class with no class or object attribute
"""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes, except for 'first_name'.
    """

    def __setattr__(self, name, value):
        """
        Override the default behavior of setting instance attributes.

        Args:
            name (str): The name of the attribute.
            value: The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute is not 'first_name' and it does not already exist.
        """
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))

        super().__setattr__(name, value)
