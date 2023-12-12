# Define a function which takes a dictionary as a parameter and returns a dictionary in which the key-value pairs are reversed.
def reverse_dict(my_dict):
    myDict2 = {value:key for (key, value) in my_dict.items()}
    return myDict2

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))

# Time Complexity: O(n)
# Space Complexity: O(n)