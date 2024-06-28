#!/usr/bin/python3
"""
This module defines a class Rectangle \
with private attributes width and height.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    ...

    Attributes:
        width (int): width of the rectangle (default is 0)
        height (int): height of the rectangle (default is 0)

    Methods:
        width(): Gets the width of the rectangle
        width(value): Sets the width of the rectangle
        height(): Gets the height of the rectangle
        height(value): Sets the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructing all the necessary attributes for the rectangle object.

        Parameters:
            width (int, optional): Width of the rectangle (default is 0)
            height (int, optional): Height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getting the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting the width of the rectangle.

        Parameters
        ----------
        value : int
            Width of the rectangle

        Raises
        ------
        TypeError
            If width is not an integer
        ValueError
            If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getting the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting the height of the rectangle.

        Parameters
        ----------
        value : int
            Height of the rectangle

        Raises
        ------
        TypeError
            If height is not an integer
        ValueError
            If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        """
        Returning the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Printing the rectangle

        Return:
            A printed rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symb = str(self.print_symbol)
        return ((symb * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """
        Returning a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Printing a message when an instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            comparing 2 rectangles
        Args:
            rect_1(Rectangle): First Rectangle
            rect_2(Rectangle): Second Rectangle
        Raises:
            TypeError: If rect_1 is not instance of Rectangle
            TypeError: If rect_2 is not instance of rectangle
        Return:
            The Biggest Rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Making a square from a rectangle
        Args:
            size (int): the size of the square
        Returns:
            (Rectangle): instance of rectangle
        """
        return cls(size, size)
