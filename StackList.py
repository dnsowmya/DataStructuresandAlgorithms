class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        revlist = self.list[::-1]
        values = [str(x) for x in revlist]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been added"

    # pop
    def pop(self):
        if self.isEmpty():
            return "No Elements"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "No Elements"
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list = None


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.pop())
print(customStack)
print(customStack)
print(customStack)
print(customStack.peek())