#!/usr/bin/env python3

# O(n)
def h_two_sum(nums, target):
    hmap = {}
    for k, v in enumerate(nums):
        if v in hmap:
            return [hmap[v], k]
        hmap[target - v] = k


# O(n^2)
def i_two_sum(nums, target):
    result = []

    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if i + j == target:
                return [nums.index(i), nums.index(j)]


nums = [2, 7, 11, 15]
target = 9

print(i_two_sum(nums, target))
print(h_two_sum(nums, target))
