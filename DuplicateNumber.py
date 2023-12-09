# Write a function to remove duplicate numbers in any array/list
def remove_duplicates(arr):
    newset = set(arr)
    return list(newset)

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

# Another approach

def rem_dup(lst):
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

print(rem_dup([1, 1, 2, 2, 3, 4, 5]))

# Time Complexity: O(n)
# Space Complexity: O(n)

# Another question
# Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct.

def contains_duplicate(nums):
    myset = set(nums)
    new_nums = list(myset)
    if nums == new_nums:
        return False
    else:
        return True

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

