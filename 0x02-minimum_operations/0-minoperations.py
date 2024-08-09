#!/usr/bin/python3
"""This module contains minOperations function"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    # no operations are needed
    if n <= 1:
        return 0

    # initialize variables
    operations = 0
    factor = 2

    while n > 1:
        # checks if the current factor divides n evenly. If it does,
        # we divide n by this factor and add the factor to our operations count
        while n % factor == 0:
            n //= factor
            operations += factor

        factor += 1

        # check if n is a prime number
        if (factor * factor > n) and (n > 1):
            operations += n
            break

    return operations
