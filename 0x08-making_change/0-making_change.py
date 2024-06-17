#!/usr/bin/python3
"""Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total."""


def makeChange(coins, total):
    if total <= 0:
        return 0
    bal = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    m = len(coins)
    while bal > 0:
        if coin_idx > m:
            return -1
        if bal - sorted_coins[coin_idx] >= 0:
            bal -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
