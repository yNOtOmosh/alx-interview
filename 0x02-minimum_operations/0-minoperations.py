#!/usr/bin/python3
"""Minimum operations."""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1

    n -= 1

    # greed
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            operations += clipboard
            clipboard = i
    return operations
