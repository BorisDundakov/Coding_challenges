''' There is an array of integers. A second array is formed by shuffling the elements of the first array
 and deleting a random element.
 Given these two arrays, find which element is missing in the second array.'''

import numpy as np


def missing_number(arr):
    arr = np.array(arr)
    array = arr.copy()
    # forming the second_array
    np.random.shuffle(arr)
    # popping item from shuffled array
    arr = np.delete(arr, 0)
    print("Shuffled array with deleted index: ", arr)
    print("Original array: ", array)
    diff = set(array) - set(arr)
    return diff


print(missing_number([1, 2, 3, 4, 5]))
