#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of,
    or an instance of a class that inherited from, the specified class.

    Args:
    - obj: Object to be checked.
    - a_class: Specified class for comparison.

    Returns:
    - True if the object is an instance of the specified class
    or its subclass; False otherwise.
    """
    return isinstance(obj, a_class)
