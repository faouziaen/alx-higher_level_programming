#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
    - obj: Object to be checked.
    - a_class: Specified class for comparison.

    Returns:
    - True if the object is an instance of the specified class;
     False otherwise.
    """
    return type(obj) is a_class
