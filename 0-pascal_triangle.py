#!/usr/bin/env python3
"""
Pascal triangle that prints out an array
"""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        print("Invalid input!")
    else:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j-1] + triangle[i - 1][j])
            triangle.append(row)
        return triangle
