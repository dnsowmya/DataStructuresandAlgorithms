import math
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        mid = self.length/2
        index = math.floor(mid)
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node

new_linked_list = LinkedList()
print(new_linked_list)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
#new_linked_list.append(40)
print(new_linked_list)
print(new_linked_list.find_middle().value)
print(new_linked_list)

# Another approach

def find_middle(self):
    slow = self.head
    fast = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Time Complexity: O(n)
# Space Complexity: O(1)
