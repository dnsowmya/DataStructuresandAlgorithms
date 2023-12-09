# Max Product of Two Integers

arr = [1, 7, 3, 4, 9, 5]


def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

print(max_product(arr))

# Another Approach

def max_prod_arr(arr):
    # Initialize 2 variables to store the 2 largest numbers
    max1, max2 = 0, 0

    # Iterate through the array
    for num in arr:
        # If current number if greater than max1, update max2 as max1 and max1 as the current number
        if num > max1:
            max2 = max1
            max1 = num
        # If current number is greater than max2 but not max1, then update max2 as current number
        elif num > max2:
            max2 = num

    # return the product of the 2 largest numbers in the array
    return max1*max2

print(max_prod_arr(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)