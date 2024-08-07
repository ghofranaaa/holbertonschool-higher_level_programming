#!/usr/bin/python3
"""Define class with using library abc"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    shape have two methods area and perimeter
    inherit from class shape.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    circle inherit from shape and calcul radius
    """

    def __init__(self, radius):
        if isinstance(radius, (int, float)):
            self.radius = abs(radius)
        else:
            raise TypeError("Radius must be a number")
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    rectangle inherit from shape define width and height
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    print area and perimeter
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)