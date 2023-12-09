# You are given an n*n 2D matrix,representing an image,rotate the image by 90 degrees clockwise. You have to rotate the image
# in-place, which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix and do the rotation.
# Example: [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# output:  [[7, 4, 1],
#           [8, 5, 2],
#           [9, 6, 3]]

import numpy as np

def matrix_rotate(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    newmatrix = [[0]*rows for i in range(rows)]
    print(newmatrix)

    # Transpose
    for i in range(rows):
        for j in range(cols):
            newmatrix[i][j] = matrix[j][i]

    # Transpose without using a new matrix
    for i in range(rows):
        for j in range(i, cols): # 0 0,0 0,1 0,2 1 1,1 1,2
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(newmatrix)
    print(matrix)

    # Reverse the rows
    for row in newmatrix:
        row.reverse()

    return newmatrix
mymatrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(matrix_rotate(mymatrix))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
