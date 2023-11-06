#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)."""


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

        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        # Check if value is less than or equal to 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
