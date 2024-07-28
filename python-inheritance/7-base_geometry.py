#!/usr/bin/python3

"""
This module extends the BaseGeometry class from the previous
exercise to include a public instance method named area
and integer_validator.
"""


class BaseGeometry:
    """
    BaseGeometry serves as a foundational class for geometric shapes.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value based on two conditions:
        it must be an integer, and it must be greater than zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
