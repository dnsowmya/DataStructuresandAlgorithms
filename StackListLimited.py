class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        revlist = self.list[::-1]
        values = [str(x) for x in revlist]
        return '\n'.join(values)

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
            return "Element inserted"

customStack = Stack(4)
print(customStack.isFull())
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack)

