#!/usr/bin/python3
"""Defines a function to dynamically add attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (any): The object to which an attribute is added.
        att (str): The name of the attribute to add to 'obj'.
        value (any): The value to assign to the attribute.
    Raises:
        TypeError: If the attribute cannot be added due to object immutability.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
