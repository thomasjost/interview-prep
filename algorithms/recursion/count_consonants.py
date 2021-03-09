#!/usr/bin/env python3
"""
Given a string, count the number of consonants.
Note a consonant is a letter that is not a vowel,
ie a letter that is not a, e, i, o, or u.
"""

input_string_1 = "abc de"
input_string_2 = "ThomasJost"
vowels = 'aeiou'


def i_count_consonants(input_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i].lower() not in vowels and input_string[i].isalpha():
            count += 1
    return count


def r_count_consonants(input_string):
    if input_string == '':
        return 0
    if input_string[0].lower() not in vowels and input_string[0].isalpha():
        return 1 + r_count_consonants(input_string[1:])
    else:
        return r_count_consonants(input_string[1:])


print(i_count_consonants(input_string_1))
print(i_count_consonants(input_string_2))
print(r_count_consonants(input_string_1))
print(r_count_consonants(input_string_2))
