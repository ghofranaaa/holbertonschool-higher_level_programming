#!/usr/bin/python3
"""
This module provides a class `BaseGeometry`.
"""


class BaseGeometry:
    """
    BaseGeometry serves as a foundational class for geometric shapes.
    It is intended to be subclassed by specific geometric shape classes.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not
        implemented.

        Raises:
            Exception: An exception with the message "area() is not
            implemented".
        """
        raise Exception("area() is not implemented")
