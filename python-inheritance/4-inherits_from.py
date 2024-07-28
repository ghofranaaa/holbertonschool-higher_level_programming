#!/usr/bin/python3

"""
This module defines a utility function, inherits_from, which checks if
an object is an instance of a class that has inherited
(directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that has inherited
    (directly or indirectly) from a_class.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - bool: True if obj is an instance of a class that has inherited
    from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
