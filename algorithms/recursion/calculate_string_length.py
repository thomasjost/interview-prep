#!/usr/bin/env python3
"""
Given a string, calculate the length of the string
"""

input_string = "ThomasJost"

print(len(input_string))


def i_calculate_length(input_string):
    count = 0
    for i in range(len(input_string)):
        count += 1
    return count


def r_calculate_length(input_string):
    if input_string == '':
        return 0
    return 1 + r_calculate_length(input_string[1:])


print(i_calculate_length(input_string))

print(r_calculate_length(input_string))
