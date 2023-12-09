# Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

list1 = [1, 2, 3]
list2 = [1, 3, 2]

str_list1 = ['a', 'b', 'c']
str_list2 = ['c', 'a', 'b']

print(permutation(str_list1,str_list2))