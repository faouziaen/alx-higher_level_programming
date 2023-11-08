#!/usr/bin/python3
"""Defines a Student class to represent student information."""


class Student:
    """Represents student details including first name,
    last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtains a dictionary representation of the Student object."""
        return self.__dict__
