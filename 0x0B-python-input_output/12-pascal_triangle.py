#!/usr/bin/python3
# 12-pascal_triangle
"""
Implements a function that returns a list of lists of integers
representing the Pascal's triangle of n:
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's
    triangle of n:

    Args:
    n (int): a number n

    Return:
    Lists of integers representing the Pascal's triangle of n:
    """
    pascal = []
    for i in range(1, n + 1):
        list = []
        for j in range(i):
            if j == 0 or j == i - 1:
                list.append(1)
            else:
                prev_list = pascal[i - 2]
                list.append(prev_list[j] + prev_list[j - 1])
        pascal.append(list)
    return pascal
