# Given a list, write a function to get first, second best scores from the list.List may contain duplicates

def first_second(my_list):
    my_list.sort(reverse=True)
    mytuple = (my_list[0],my_list[1])
    return mytuple

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList))

# Another approach
"""
def first_sec(my_list):
    max1,max2 = float('-Inf'), float('-Inf')

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2

print(first_sec(myList))
"""
# Time Complexity: O(n)
# Space Complexity: O(1)

