#!/usr/bin/env python3
def spreadsheet_encode_column(column):
    num = 0
    count = len(column) - 1

    for s in column:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num


# Tests
print(spreadsheet_encode_column("A"))
print(spreadsheet_encode_column("AA"))
print(spreadsheet_encode_column("ZZ"))
