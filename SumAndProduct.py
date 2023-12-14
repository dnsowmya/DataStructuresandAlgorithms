# Write a function that calculates the sum and product of all elements in a tuple of numbers
def sum_product(input_tuple):

    sum_tuple = sum(input_tuple)
    prod = 1
    for i in range(len(input_tuple)):
        prod = prod * input_tuple[i]

    return sum_tuple, prod

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

# Time Complexity: O(n)
# Space Complexity: O(1)