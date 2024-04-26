#!/usr/bin/python3
"""Pascal's triangle."""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for k in range(n):
        row = [1] * (k + 1)
        for l in range(1, k):
            row[l] = triangle[k - 1][l -1] + triangle[k - 1][l]
        triangle.append(row)

    return triangle
