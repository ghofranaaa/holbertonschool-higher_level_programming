#!/usr/bin/python3
"""
This module defines a Square class with getter and setter for size.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initializing the square with a private size attribute.
        Validating size to be an integer and >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getting the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setting the size of the square.
        Validating size to be an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculating the area of the square.
        """
        return self.__size ** 2
