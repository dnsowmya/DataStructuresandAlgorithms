def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if (cb(arr[0])):
        print(cb(arr[0]))
        return True
    else:
        print("1")
        return someRecursive(arr[1:], cb)

print(someRecursive([2,4], isOdd))