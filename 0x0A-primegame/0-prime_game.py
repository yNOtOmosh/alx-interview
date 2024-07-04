#!/usr/bin/python3
"""Prime Game"""


def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0], is_prime[1] = False, False
    primes = []
    for p in range(n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        available = list(range(1, n + 1))
        moves = 0
        for p in primes:
            if p > n:
                break
            if p in available:
                moves += 1
                for multiple in range(p, n + 1, p):
                    if multiple in available:
                        available.remove(multiple)

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
