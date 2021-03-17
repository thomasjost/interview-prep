#!/usr/bin/env python3

def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[n - k:] + nums[:n-k]
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
print(rotate(nums, 3))
