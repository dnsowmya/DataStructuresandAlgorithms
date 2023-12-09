# Create a new list containing all the elements from the original list excluding the first and last elements

def middle(lst):
    # return a new list containing all the elements from the original list excluding the first and last elements
    return lst[1:-1]

mylist = [1, 2, 3, 4]

print(middle(mylist))

# Time Complexity: O(n)
# Space Complexity: O(n)