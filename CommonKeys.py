# Function which takes 2 dictionaries as parameters and merge them and sum the values of common keys
def merge_dicts(dict1, dict2):

    dict3 = dict1.copy()

    for key_d2,value_d2 in dict2.items():
        dict3[key_d2] = dict3.get(key_d2,0) + value_d2


    print(dict3)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)

# Time Complexity: O(n+m)
# Space Complexity: O(n+m)
