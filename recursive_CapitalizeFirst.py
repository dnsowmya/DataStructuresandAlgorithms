def capitalizeFirst(arr):
    res = []
    if len(arr) == 0:
        return res
    res.append(arr[0].capitalize())
    return res+capitalizeFirst(arr[1:])

print(capitalizeFirst(['car','taco','banana']))

def capitalizeWords(arr):
    res = []
    if len(arr) == 0:
        return res
    res.append(arr[0].upper())
    return res+capitalizeWords(arr[1:])

words = ['i','am','learning','recursion']
print(capitalizeWords(words))