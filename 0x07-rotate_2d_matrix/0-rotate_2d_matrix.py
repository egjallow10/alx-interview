#!/usr/bin/python3
""" two 2d rotation of 90 deg"""


def rotate_2d_matrix(matrix):
    array_len = len(matrix)

    for i in range(array_len):
        for j in range(i, array_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(array_len):
        matrix[i] = matrix[i][::-1]
