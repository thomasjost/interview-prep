#!/usr/bin/env python3
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    length = 1
    previous = nums[0]
    idx = 1

    for i in range(1, len(nums)):
        if nums[i] != previous:
            length += 1
            previous = nums[i]
            nums[idx] = nums[i]
            idx += 1
    return length


nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]
print(removeDuplicates(nums))
