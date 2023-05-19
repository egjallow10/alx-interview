#!/usr/bin/python3
"""
makeChange method
"""


def makeChange(coins, total):
    """fewenumber of coin need"""
    number_of_coins = 0
    amount = 0
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)

    for coin in coins:
        while amount + coin <= total:
            amount += coin
            number_of_coins += 1
        if amount == total:
            return number_of_coins
    return -1
