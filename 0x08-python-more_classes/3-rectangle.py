#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with # character."""
        rect_str = ''
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            rect_str += '#' * self.__width + '\n'
        return rect_str[:-1]  # Remove the last newline character

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'
