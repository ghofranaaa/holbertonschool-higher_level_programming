#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle represents a rectangle with a specified width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self._width = width
        self._height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self._width * self._height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self._width}/{self._height}"
