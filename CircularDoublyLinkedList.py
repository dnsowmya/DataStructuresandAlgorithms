class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

# Creation of Circular Doubly Linked List

    def createCDLL(self, Value):
        new_node = Node(Value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return "The Circular Doubly Linked List is created Successfully!"

# Insertion method in Circular Doubly Linked List

    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return "The node has been successfully inserted"

# Traversal of Circular Doubly Linked List
    def traversalCDLL(self):
        if self.head is None:
            print("There is no node for traversal")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next

# Reversal Traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
       if self.head is None:
           print("There are no nodes")
       else:
           temp_node = self.tail
           while temp_node:
               print(temp_node.value)
               if temp_node == self.head:
                   break
               temp_node = temp_node.prev

# Delete a node from Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There are no Nodes")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curr_node = self.head
                index = 0
                while index < location - 1:
                    curr_node = curr_node.next
                    index += 1
                    curr_node.next = curr_node.next.next
                    curr_node.next.prev = curr_node
                print("The Node has been Successfully deleted")

# Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There are no elements to delete")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The Circular Doubly Linked List has been Successfully deleted")



circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(10))
print([node.value for node in circularDLL])
circularDLL.insertCDLL(20,1)
print([node.value for node in circularDLL])
print(circularDLL.traversalCDLL())
print(circularDLL.reverseTraversalCDLL())
print(circularDLL.deleteNode(0))
print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])
