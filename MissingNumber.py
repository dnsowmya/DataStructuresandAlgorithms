# Find the missing number in an array of n series numbers

import numpy as np
def findMissing(arr,n):
    n_series_sum = n*(n+1)/2

    arr_total = sum(arr)

    missing_num = n_series_sum - arr_total

    return missing_num

myarray = np.array([1,2,3,4,6])
print(findMissing(myarray,6))