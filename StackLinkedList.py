class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "No Element"
        else:
            nodevalue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue

    def peek(self):
        if self.isEmpty():
            return "No Element"
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.pop())
print(customStack)
print(customStack.peek())
print(customStack)