#!/usr/bin/python3
"""
This module contains pascal_triangle(n) function
that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns Pascal’s triangle of n"""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            # edges of the triangle
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                value = triangle[i - 1][j] + triangle[i - 1][j - 1]
                triangle[i].append(value)
    return triangle
