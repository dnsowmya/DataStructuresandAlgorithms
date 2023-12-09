# Leet Code - Find Pairs or Two Sum

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

myList = [1,2,3,4,5]
findPairs(myList, 6)

#Leet Code Solution

def two_sum(arr, target):
    checked_values = {}

    for index, value in enumerate(arr):
        remaining_sum = target - value

        if remaining_sum in checked_values:
            return [checked_values[remaining_sum], index] # return indices

        checked_values[value] = index

newList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(two_sum(newList, 7))

#Time Complexity is O(n)

# another question
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

def pair_sum(myList, sum):

    output_list = []
    str_val = ""

    for num, value in enumerate(myList):
        rem_value = sum - value

        if rem_value in myList[num:]:
            str_val = str(value) + '+' + str(rem_value)
            output_list.append(str_val)

    return output_list

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

def pair_sum_new(myList, sum):
    #return list(f'{i}+{7-i}' for i in myList if 7-i in myList)
    return list(f'{i}+{7-i}' for i in myList if 7-i in myList)

print(pair_sum_new([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
