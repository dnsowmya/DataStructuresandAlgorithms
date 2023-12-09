import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)
my_array1.insert(0, 6)
print(my_array1)

import numpy as np

np_array = np.array([],dtype = int)
print(np_array)
np_array1 = np.array([1,2,3,4])
print(np_array1)

from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

print(arr1)
print(arr2)

arr1.insert(2,9)
print(arr1)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

def accessElement(array, index):
    if index >= len(array):
        print("There is no element in this index")
    else:
        print(array[index])

accessElement(arr1,7)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr1,8))

arr1.remove(3)

print(arr1)

# Create an array and Traverse

my_array2 = array('i', [1,2,3,4,5])

for i in my_array2:
    print(i)

# Access individual elements through indexes
print("Step 2")
print(my_array2[0])

# Append any value to the array using append() method
print("Step 3")
my_array2.append(6)

print(my_array2)

# Insert value in an array using insert() method
print("Step 4")
my_array2.insert(3, 11)
print(my_array2)

# Extend Python array using extend() method
print("Step 5")
my_array3 = array('i',[10,11,12])
my_array2.extend(my_array3)
print(my_array2)

# Add items from list into array using fromlist() method
print("Step 6")
tempList = [20,21,22]
my_array2.fromlist(tempList)
print(my_array2)

# Remove any array element using remove() method
print("Step 7")
my_array2.remove(22)
print(my_array2)

# Remove last element using pop() method
print("Step 8")
my_array2.pop()
print(my_array2)

# Fetch any element using index() method -- returns the index value
print("Step 9")
print(my_array2.index(20))

# Reverse a python array using reverse() method
print("Step 10")
my_array2.reverse()
print(my_array2)

# Get array buffer information through buffer_info() method
print("Step 11")
print(my_array2.buffer_info())

# Check the number of occurrences of an element using count() method
print("Step 12")
print(my_array2.count(11))

# Convert array to string using tobytes() method
print("Step 13")
strTemp = my_array2.tobytes()
print(strTemp)
ints = array('i')
ints.frombytes(strTemp)
print(ints)

# Convert array to a python list with same elements using tolist() method
print("Step 14")
print(my_array2.tolist())

# Slice elements from an array
print("Step 15")
print(my_array2[1:4])

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(f"Test: {twoDArray[0]}")
twoDArray5 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"First Row: {twoDArray5[0]}")

twoDArray2 = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1) #axis =0 is a row
print(twoDArray2)

twoDArray3 = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(twoDArray3)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 1, 2)

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTDArray(twoDArray)

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element is not found'

print(searchTDArray(twoDArray, 14))

twoDArray4 = np.delete(twoDArray, 0, axis = 0)
print(twoDArray4)

