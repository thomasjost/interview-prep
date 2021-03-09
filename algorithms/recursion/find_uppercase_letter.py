#!/usr/bin/env python3
"""
Given a string, find the first uppercase character.
Solve using both an iterative and recursive solution.
"""

input_str_1 = "thomasJost"
input_str_2 = "ThomasJost"
input_str_3 = "thomasjost"


def i_find_uppercase(input_string):
    for i in range(len(input_string)):
        if input_string[i].isupper():
            return input_string[i]
    return "No uppercase character found"


def r_find_uppercase(input_string, idx=0):
    if input_string[idx].isupper():
        return input_string[idx]
    if idx == len(input_string) - 1:
        return "No uppercase character found"
    return r_find_uppercase(input_string, idx + 1)


print(i_find_uppercase(input_str_1))
print(i_find_uppercase(input_str_2))
print(i_find_uppercase(input_str_3))

print(r_find_uppercase(input_str_1))
print(r_find_uppercase(input_str_2))
print(r_find_uppercase(input_str_3))
