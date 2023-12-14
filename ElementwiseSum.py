def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(t1, t2))
    return result

# Time Complexity: O(n)
# Space Complexity: O(n)
# Another approach
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

print(tuple(map(sum, (zip(tuple1, tuple2)))))

# Time Complexity: O(n)
# Space Complexity: O(n)
