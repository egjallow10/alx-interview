#!/usr/bin/python3
"""
function that calculates the fewest number of
operations
"""


def minOperations(n):
    """Return the minimal operation"""
    if n <= 1:
        return 0

    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    num_ops = sum(factors)

    if num_ops == 0:
        return 0

    return num_ops
