#!/usr/bin/python3
"""
Pascal's Triangle in Python
"""


def pascal_triangle(n):
    """
    returns a list of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        mylist = [1]

        if i == 0:
            triangle.append(mylist)
            continue
        else:
            prev_row = triangle[-1]
            for j in range(1, i):
                nex = prev_row[j - 1] + prev_row[j]
                mylist.append(nex)
        mylist.append(1)
        triangle.append(mylist)

    return triangle
