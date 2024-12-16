#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    """
    function - determines the winner of the prime game
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)  # Get the largest value of n in nums
    if max_n < 2:
        return "Ben"  # Maria cannot make a move if n < 2

    # Step 1: Compute primes up to max_n using the Sieve of Eratosthenes
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
