# How to create a Tuple?

newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple)

Tuple2 = ('a',)
print(Tuple2)

Tuple3 = tuple()
print(Tuple3)

Tuple4 = tuple('abcde')
print(Tuple4)

print(newTuple[-1])

print(newTuple[1:3])

for i in newTuple:
    print(i)

for i in range(len(newTuple)):
    print(newTuple[i])

print('f' in newTuple)

print(newTuple.index('a'))

def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The element is found at {i} index"
    return 'The element is not found'

print(searchTuple(newTuple, 'f'))

myTuple = (1,4,3,2,5,2)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1)

print(myTuple * 4)

print(4 in myTuple)

print(myTuple.count(2))
print(myTuple.index(4))

print(len(myTuple))

print(max(myTuple))

print(min(myTuple))

print(tuple([1,2,3,4]))

list1 = [0,1,2,3,4,5,6,7]

list1[1] = 3
list1 = [7,6,5,4,3,2,1,0]

del list1[0]

print(list1)

tuple1 = 0,1,2,3,4,5,6,7

tuple1 = 7,8,9,0

print(tuple1)

list2 = [(1,2), (3,4), (5,6)]
print(list2)

tuple2 = ([1,2], [3,4], [5,6])
print(tuple2)

tuple3 = ((1,2), (3,4), (5,6))
print(tuple3)