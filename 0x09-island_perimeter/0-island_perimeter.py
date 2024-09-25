#!/usr/bin/python3
"""
This module contains island_perimeter(grid) function that
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Params:
        grid: is a list of list of integers 0 for water 1 for land
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check vertical sides
                if i == 0 or not grid[i - 1][j]:  # top
                    perimeter += 1
                if i == (rows - 1) or not grid[i + 1][j]:  # bottom
                    perimeter += 1

                # check horizontal sides
                if j == 0 or not grid[i][j - 1]:  # left
                    perimeter += 1
                if j == (cols - 1) or not grid[i][j + 1]:  # right
                    perimeter += 1

    return perimeter
