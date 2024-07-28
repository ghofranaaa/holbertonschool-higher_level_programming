#!/usr/bin/python3

"""
This module defines a utility function for looking up
attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of attributes and methods of the given object."""
    return list(dir(obj))
