import numpy as np

integers = [1, 2, 3, 4]
print(integers)

stringList = ['Milk', 'Cheese', 'Butter']
print(stringList)

mixedList = [1, 1.5, 'Spice']
print(mixedList)

nestedList = [1, 2, 3, 4, [1.5, 1.6], ['DeleteSingleLinkedList.py']]
print(nestedList)

empty = []
print(empty)

intList = [1,2,3,4]
print(intList)

stringList = ['milk','cheese','butter']
print(stringList)

mixedList = [3,3.7,'DeleteSingleLinkedList.py']
print(mixedList)

nestedList = [1,2,3,4,1.5,1.6,['DeleteSingleLinkedList.py']]
print(nestedList)

shoppingList = ['Milk','Cheese','Butter']
print(shoppingList[0])
print('Milk' in shoppingList)

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)

myList.insert(0,11)
print(myList)

myList.append(15) #  mylist = myList + [15] another way to append an element
print(myList)

myList2 = [11,12,13,14]
myList.extend(myList2)
print(myList)

print(myList[0:2])

myList[0:2] = ['x','y']
print(myList)

myList.pop(1)
print(myList)

del myList[1]
print(myList)

del myList[0:2]
print(myList)

myList.remove(4)
print(myList)

target = 5
if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

def linear_search(plist,ptarget):
    for i, value in enumerate(plist):
        if value == ptarget:
            return i
    return -1

print(linear_search(myList,target))

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

d = [0]
d = d * 4
print(d)
print("Length of the list a is: ", len(a))
print("Max value of List a is:", max(a))
print("Min value in List a is:", min(a))
print("Sum of all the values in List a is:",sum(a))
print("Average value in List a is:", sum(a)/len(a))

mylist3 = []
input_var = "done" # changing for DeleteSingleLinkedList.py
total = 0
average = 0
while input_var != 'done':
    #input_var = input("Please enter a number: ")
    if input_var != "done":
        mylist3.append(float(input_var))
    else:
        total = sum(mylist3)
        average = total/len(mylist3)

print(mylist3)
print(f"Sum = {total} and Average = {average}")

a = 'spam'
b = list(a)
print(b)

string1 = 'spam spam spam'
b1 = string1.split()
print(b1)

string2 = 'spam1-spam2-spam3'
delimiter = '-'
b2 = string2.split(delimiter)
print(b2)
print(delimiter.join(b2))

myArray = np.array([1, 2, 3, 4, 5, 6])
print(myArray)
print(myArray/2)

myArray2 = np.array([1,2,3,4,5,6,'a']) # This will convert all the numbers to strings as Array does not support multiple data types
myList4 = [1,2,3,4,5,6,'a']

prev_list = [1,2,3]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

language = 'Python'
new_list1 = [letter for letter in language]
print(new_list1)

prev_list1 = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list2 = [i for i in prev_list1 if i > 0]
print(new_list2)

new_list3 = [i**2 for i in prev_list1 if i < 0]
print(new_list3)

sentence = "My name is DN"

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('a'))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

new_list4 = [i if i > 0 else 0 for i in prev_list1]
print(new_list4)

lst = [1, 2, 3, 4]
new_list5 = lst[1:-1]
print(new_list5)




