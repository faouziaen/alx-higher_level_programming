#!/usr/bin/python3
"""Pascals triangle function."""


def pascal_triangle(n):
    """
    Generates Pascal's triangle for a given n.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle
