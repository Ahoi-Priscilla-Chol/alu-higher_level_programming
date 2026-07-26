#!/usr/bin/python3
"""Defines a function that returns Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle of n rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        A list of lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
