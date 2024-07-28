#!/usr/bin/python3
"""
This module defines a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square with a specified side length.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.
        """
        self.integer_validator('size', size)
        self._size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self._size ** 2
