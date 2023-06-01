#!/usr/bin/python3
""" choosing a prime number from the set"""


def isWinner(x, nums):
    """determine who the winner of each game"""

    if not nums or x < 1:
        return None
    max_num = max(nums)
    primes = [True for _ in range(max_num + 1)]
    # Using the Sieve of Eratosthenes algorithm to mark prime numbers

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    primes[0] = primes[1] = False
    # Counting the number of primes up to each index

    prime_counts = [0] * len(primes)
    count = 0
    for i in range(len(primes)):
        if primes[i]:
            count += 1
        prime_counts[i] = count
    # Counting the number of odd prime counts in the given list

    player1 = 0
    for num in nums:
        if prime_counts[num] % 2 == 1:
            player1 += 1
    # Comparing the counts to determine the winner

    if player1 * 2 == len(nums):
        return None
    elif player1 * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
