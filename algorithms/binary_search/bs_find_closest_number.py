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

    midpoint: 5
    right of midpoint: 6 - 4 = 2
    left of midpoint: 2 - 4 = 2

    midpoint: 2
    right of midpoint: 5 - 4 = 1
    left of midpoint: -
"""


def find_closest_number(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_number = None

    # Edge cases for empty list or when list is only one element
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        # Limit reading to within bounds of list, obtain left & right
        # difference values
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # Check if the absolute value between left and right elements
        # are smaller than any seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = A[mid + 1]

        # Move the midpoint accordingly as is done via binary search
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            return A[mid]
    return closest_number


A = [1, 2, 4, 5, 6, 6, 8, 9]

x = find_closest_number(A, 10)
print(x)
A = [2, 5, 6, 7, 8, 8, 9]

x = find_closest_number(A, 4)
print(x)
