#!/usr/bin/python3
"""
This module contains rotate_2d_matrix() which rotate
a 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): A square 2D matrix to be rotated.

    Returns:
        The function doesn't return anything.
        it modifies the input matrix in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
