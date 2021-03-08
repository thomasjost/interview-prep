#!/usr/bin/env python3

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 28

# Linear search - O(n)


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# iterative binary search - O(log n)


def i_binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Recursive binary search - O(log n)


def r_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return r_binary_search(data, target, low, mid - 1)
        else:
            return r_binary_search(data, target, mid + 1, high)


print(i_binary_search(data, target))
print(r_binary_search(data, target, 0, len(data)))
