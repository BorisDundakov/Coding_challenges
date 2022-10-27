"""Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
 The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 1.py. The input [1, 1.py, 0] should give 3."""


def find_missing_positive(arr):
    num = 1
    while num in set(arr):
        num += 1
    return num


find_missing_positive([1, 2, 3, 4, 4, 2, 6])
