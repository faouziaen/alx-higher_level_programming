#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list object containing the available attributes
    and methods of an object.

    Args:
    - obj: An object whose attributes and methods need to be inspected.

    Returns:
    - A list of strings containing the attributes and methods of the object.
    """
    return dir(obj)
