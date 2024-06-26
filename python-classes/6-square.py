#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes.
"""


class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with size and position attributes.
        Validate size to be an integer and >= 0.
        Validate position to be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getting the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setting the position of the square.
        Validating position to be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculating the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Printing the square with the character #.
        If the size is 0, print an empty line.
        Positioning the square using spaces.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
