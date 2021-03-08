#!/usr/bin/env python3
"""
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

Given an array of "n" distinct integers sorted in ascending order, write a
function that returns a "fixed point" in the array. If there is not a
fixed point return "None".
"""

# Time complexity: O(n)
# Space complexity: O(1)


def linear_find_fixed_point(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# Time complexity: O(log n)


def find_fixed_point(A):
    low, high = 0, len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


# Fixed point is 3:
# A = [-10, -5, 0, 3, 7]

# print(find_fixed_point(A))
# Fixed point is 0:
# A = [0, 2, 5, 8, 17]

# print(find_fixed_point(A))
# # No fixed point, return "None":
A = [-10, -5, 3, 4, 7, 9]

print(find_fixed_point(A))
