#!/usr/bin/env python3
"""
Given two numbers, find their product using recursion
"""
x = 500
y = 2000


def r_product(x, y):
    if y == 0:
        return 0
    if x < y:
        return r_product(y, x)
    return x + r_product(x, y - 1)


print(r_product(x, y))
