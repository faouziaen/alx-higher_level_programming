#!/usr/bin/python3
"""Module for the matrix_divided function."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements/ by div,
    rounded to 2 dec places.

    Raises:
        TypeError: If matrix is not a list of lists containing ints or floats.
        TypeError: If sublists in the matrix are not all of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    if len(row) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")
    for element in row:
        if not isinstance(element, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
