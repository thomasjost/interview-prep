#!/usr/bin/env python3
"""
Given an array of sorted integers. We need to find the closest value to the
given number.

Array may contain duplicate values and negative numbers.

Examples:
    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5

    midpoint: 7
    right of midpoint: 8 - 4 = 4
    left of midpoint: 6 - 4 = 2
"""


def find_closest_number(A, target):
    low = 0
    high = len(A) - 1


A = [1, 2, 4, 5, 6, 6, 8, 9]
A = [2, 5, 6, 7, 8, 8, 9]
