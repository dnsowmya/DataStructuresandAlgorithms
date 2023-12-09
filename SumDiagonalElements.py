# Given 2D list, calculate the sum of diagonal elements
def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Initialize the sum to 0
    sum = 0

    # Iterate through the rows of matrix
    for i in range(rows):
        # Add the diagonal element to the sum
        sum += matrix[i][i]
    return sum

myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))

# Time Complexity: O(n)
# Space Complexity: O(1)