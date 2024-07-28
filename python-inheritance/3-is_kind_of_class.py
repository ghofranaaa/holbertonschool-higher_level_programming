#!/usr/bin/python3

"""
This module provides a utility function, is_kind_of_class,
which checks if an object is an instance of a specified
class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass thereof.

    Parameters:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - bool: True if obj is an instance of a_class or a subclass of
    a_class, False otherwise.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
