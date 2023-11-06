#!/usr/bin/python3
"""Square that inherits from Rectangle (9-rectangle.py)"""


class BaseGeometry:
    """
    A class named BaseGeometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception if called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class named Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle object with width and height.

        Arguments:
        - width: Width of the rectangle (positive integer).
        - height: Height of the rectangle (positive integer).
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        String representation of the Rectangle object.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class named Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the Square object with a size.

        Arguments:
        - size: Size of the square (positive integer).
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        String representation of the Square object.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
