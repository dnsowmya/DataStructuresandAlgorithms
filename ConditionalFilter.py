# Define a function that takes a Dictionary as a parameter and returns a dictionary with elements based on a condition
def filter_dict(my_dict, condition):

    myDict3 = {key:value for (key,value) in my_dict.items() if(condition(key,value))}
    return myDict3

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(filter_dict(my_dict, lambda k,v: v % 2 == 0))

# Time Complexity: O(n)
# Space Complexity: O(1)