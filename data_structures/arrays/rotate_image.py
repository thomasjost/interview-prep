#!/usr/bin/env python3

def rotate(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    # invert the rows
    for i in range(rows // 2):
        matrix[i], matrix[columns-i-1] = matrix[columns-i-1], matrix[i]

    # transpose the rows
    for i in range(rows):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate(matrix))
