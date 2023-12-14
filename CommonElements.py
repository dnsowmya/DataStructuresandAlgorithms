
def common_elements(tuple1, tuple2):

    len_tup1 = len(tuple1)
    len_tup2 = len(tuple2)
    return tuple(set(tuple1) & set(tuple2))
    #print(tuple(tuple1[i] for i in range(len_tup1) for j in range(len_tup2) if tuple1[i] == tuple2[j]))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)

# Time Complexity: O(n)
# Space Complexity: O(n)