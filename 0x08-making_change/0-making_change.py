#!/usr/bin/python3
"""
This module contains makeChange() function that determine
the fewest number of coins needed to meet a given amount
using dynamic programming
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    using dynamic programming (Bottom Up)

    Params:
        coins: list of int
        total: int

    Return (int): fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # This table will store the answer to our sub problems
    # Initialize dp array with infinity, except dp[0] = 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Solve every subproblem from 1 to total
    for i in range(1, total + 1):
        # For each coin we are given
        for coin in coins:
            # If it is less than or equal to the sub problem total
            if coin <= i:
                # check if it gives us a more optimal solution
                dp[i] = min(dp[i], dp[i - coin] + 1)

    """
    dp[total] holds the answer
    
    Otherwise, If we do not have an answer then dp[total] will be INFINITY
    meaning dp[total] > total will be true. So we return -1
    """
    return -1 if dp[total] > total else dp[total]
