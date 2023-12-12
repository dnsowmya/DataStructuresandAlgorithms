# Creating Dictionary
import random

my_dict = dict()
print(my_dict)

my_dict2 = {}
print(my_dict2)

eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)

eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng_sp2)

eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)

# Update/add an element in the dictionary

myDict = {'name': 'Edward', 'age': 26}
myDict['age'] = 27
print(myDict)

myDict['address'] = 'London'
print(myDict)

def traverseDict(dict):

    for key in dict:
        print(key, dict[key])

# Traversing through a Dictionary
traverseDict(myDict)

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'Does not exist'

print(searchDict(myDict, 26))

# Delete an element from a Dictionary

del myDict['age']
print(myDict)

removed_element = myDict.pop('addre',None)
print(removed_element)

removed_element1 = myDict.popitem()
print(removed_element1)

#myDict.clear()
print(myDict)

myDict2 = myDict.copy()
print(myDict2)

myDict3 = {}.fromkeys([1,2,3], 0)
print(myDict3)

myDict = {'name': 'Edward', 'age': 26}

print(myDict.get('address', 27))

print(myDict.items())

print(myDict.keys())

print(myDict.popitem())

print(myDict.setdefault('name1','added'))

print(myDict.pop('age','not'))
print(myDict)

print(myDict.values())

myDict4 = {'a':1, 'b':2, 'c':3, 3:'three'}

myDict.update(myDict4)

print(myDict)

print(3 in myDict)
print(('three' in myDict.values()))
print('ten' not in myDict.values())

print(len(myDict))

print(all(myDict))

myDict5 = {1: "zero", 0: "False"}
print(all(myDict5))

print(any(myDict))
print((any(myDict5)))

print(sorted(myDict5))

city_names = {'Paris', 'London', 'Rome', 'Berlin', 'Madrid'}

myDict6 = {city:random.randint(20, 30) for city in city_names}
print(myDict6)

myDict7 = {city:value for (city, value) in myDict6.items() if value > 22}
print((myDict7))

