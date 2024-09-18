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

    # Loop through each coin in the list
    for coin in coins:
        """
        For each coin, update the dp array for values
        from the coin value up to the total
        """
        for value in range(coin, total + 1):
            """
            Update dp[value] as the minimum between its current
            value and dp[value - coin] + 1
            
            dp[value - coin] gives the number of coins needed
            to reach the remainder (value - coin)
            """
            dp[value] = min(dp[value], dp[value - coin] + 1)

    """
    If dp[total] is still infinity, it means it's impossible to reach
    the total with the given coins, return -1
    Otherwise, return dp[total], which holds the number of coins needed
    """
    return dp[total] if dp[total] != float("inf") else -1
