# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
def get_diagonal(tup):

    rows = len(tup)
    x = tuple(tup[i][i] for i in range(rows))

    return x

input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

# Time Complexity: O(n)
# Space Complexity: O(n)