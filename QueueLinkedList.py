class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "No nodes"
        else:
            temp_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temp_node

    def peek(self):
        if self.isEmpty():
            return "No Nodes"
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())



