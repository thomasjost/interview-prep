#!/usr/bin/env python3

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        profit += max(prices[i] - prices[i - 1], 0)

    return profit


prices = [0, 1, 2, 3, 4, 5]
print(maxProfit(prices))
