# How to check if an array contains a number

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def find_number(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            print(i)

find_number(myArray, 13)