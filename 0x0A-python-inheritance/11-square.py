#!/usr/bin/python3
"""Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named BaseGeometry."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size