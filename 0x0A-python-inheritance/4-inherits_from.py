#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
    - obj: Object to be checked.
    - a_class: Specified class for comparison.

    Returns:
    - True if the object is an instance of a class
    that inherited from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
