#!/usr/bin/python3
"""
This module multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(matrix_a, matrix_b):
    """
    multiply 2 matrix that is given
    Args:
        matrix_a: input first matrix
        matrix_b: input second matrix
    Returns:
        return matrix_a * matrix_b
    """
    return numpy.matmul(matrix_a, matrix_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
