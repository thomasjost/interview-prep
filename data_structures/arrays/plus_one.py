#!/usr/bin/env python3

def plusOne(digits):
    num = ""
    for i in digits:
        num += str(i)
    num = int(num)
    num += 1
    num = str(num)
    result = []
    for i in num:
        result.append(int(i))
    return result


digits = [9]
print(plusOne(digits))
