#!/usr/bin/python3
"""
This module contains isWinner() function that
determines the winner of multiple rounds of the prime game.
"""


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of the prime game.

    Args:
        x: Number of rounds.
        nums: List of integers representing the upper limit of each round.

    Returns:
        The player who won the most rounds ("Maria" or "Ben"),
        or None if tied.
    """
    if x <= 0 or not nums:
        return None

    # Find the maximum value in nums to generate primes up to that number
    max_num = max(nums)

    # Step 1: Sieve of Eratosthenes to generate a list of primes up to max_num
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    # Using Sieve of Eratosthenes to mark non-primes
    for start in range(2, int(max_num**0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, max_num + 1, start):
                primes[multiple] = False

    # Step 2: Precompute the number of prime choices up to each number n
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the count of prime numbers up to n is odd,
        # Maria wins (since she starts first)
        # If it's even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
