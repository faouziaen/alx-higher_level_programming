#!/usr/bin/python3
"""Defines a class MyInt that inherits from
int but inverses the equality operators."""


class MyInt(int):
    """Inverts int operators == and != to achieve opposite behavior."""

    def __eq__(self, value):
        """Overrides the == operator to produce the inverse behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator to produce the inverse behavior."""
        return self.real == value
