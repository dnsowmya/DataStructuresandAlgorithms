# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

input_tuple = ('Hello','World','from','Python')
output_string = concatenate_strings(input_tuple)
print(f"'{output_string}'")

# Time Complexity: O(n)
# Space Complexity: O(n)
