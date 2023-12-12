
def check_same_frequency(list1, list2):
    # TODO
    list1_counts = {}
    list2_counts = {}
    for i in range(len(list1)):
        list1_counts[list1[i]] = list1.count(list1[i])

    print(list1_counts)

    for j in range(len(list2)):
        list2_counts[list2[j]] = list2.count(list2[j])

    print(list2_counts)

    return list1_counts == list2_counts



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

# Another approach:

"""def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)"""

# Time Complexity: O(n1+n2+min(m1,m2))
# Space Complexity: O(m1+m2)
# n1: Number of elements in List1
# n2: Number of elements in List2
# m1: Number of distinct elements in List1
# m2: Number of distinct elements in List2