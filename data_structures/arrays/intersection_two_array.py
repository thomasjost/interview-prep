#!/usr/bin/env python3

def intersect(nums1, nums2):
    set1 = {}

    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    for i in nums1:
        if i not in set1:
            set1[i] = 1
        else:
            set1[i] += 1

    intersect = []
    for i in nums2:
        if i in set1 and set1[i]:
            set1[i] -= 1
            intersect.append(i)

    return intersect


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
print(intersect(nums1, nums2))
