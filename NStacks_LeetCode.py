# Implement N > 0 stacks using a single array to store all stack data.No stack should be full unless the entire
# array is full
"""
N = 3
stacks.push(0, 5)
stacks.push(0 ,6)
stacks.push(1, 7)
stacks.pop(0)
stacks.push(2, 8)
topOfStack = {0, 2, -1}
stackData  = {5, 6, 7, 0, 0, 0}
nextIndex  = {-1, 3, -1, 4, 5, -1}
nextAvailable = 1
"""


class Stacks:

    def __init__(self, numStacks, capacity):
        self.numStacks = numStacks
        self.capacity = capacity
        self.topOfStack = [-1] * self.numStacks
        self.stackData = [0] * self.capacity
        self.nextIndex = [0] * self.capacity
        for i in range(self.capacity):
            self.nextIndex[i] = i+1
            i += 1
        self.nextIndex[self.capacity-1] = -1
        self.nextAvailable = 0

        print(self.topOfStack)
        print(self.stackData)
        print(self.nextIndex)
        print(self.nextAvailable)

    def push(self, stack, value):
        if stack < 0 or stack >= self.numStacks:
            raise ValueError("Stack number is invalid.")
        elif self.nextAvailable < 0:
            return "Stack is Full!"

        curr_index = self.nextAvailable
        self.nextAvailable = self.nextIndex[curr_index]
        self.stackData[curr_index] = value
        self.nextIndex[curr_index] = self.topOfStack[stack]
        self.topOfStack[stack] = curr_index

        print(self.topOfStack)
        print(self.stackData)
        print(self.nextIndex)
        print(self.nextAvailable)

    def pop(self, stack):
        if stack < 0 or stack >= self.numStacks:
            raise ValueError("Stack number is invalid.")
        elif self.topOfStack[stack] < 1:
            raise ValueError("Stack is empty.")

        curr_index = self.topOfStack[stack]
        value = self.stackData[curr_index]
        self.topOfStack[stack] = self.nextIndex[curr_index]
        self.nextIndex[curr_index] = self.nextAvailable
        self.nextAvailable = curr_index
        return value


newStack = Stacks(3,6)
newStack.push(2, 10)
