def flatten(arr):
    res = []
    for i in range(len(arr)):
        if type(arr[i]) is list:
            res.extend(flatten(arr[i]))
        else:
            res.append(arr[i])
    return res

print(flatten([1, 2, 3, [4, 5]]))