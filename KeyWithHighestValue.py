# Define a function which takes a dictionary as a parameter and returns the key with the highest value in dictionary
def max_value_key(my_dict):
    # TODO
    myDict = {'max_value':0, 'key':0}
    for key,value in my_dict.items():
        if value > myDict['max_value']:
            myDict['max_value'] = value
            myDict['key'] = key

    return myDict['key']

my_dict = {'a':5, 'b':9, 'c':2}
max_value = max_value_key(my_dict)

# Another approach
"""
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)
"""

