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

    def reverse(self):
        temp_1_node_prev = None
        temp_2_node_curr = self.head
        temp_3_node_next = None

        while temp_2_node_curr is not None:
            temp_3_node_next = temp_2_node_curr.next
            temp_2_node_curr.next = temp_1_node_prev
            temp_1_node_prev = temp_2_node_curr
            temp_2_node_curr = temp_3_node_next
        self.head = temp_1_node_prev




new_linked_list = LinkedList()
print(new_linked_list)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
new_linked_list.reverse()
print(new_linked_list)

# Time Complexity: O(n)
# Space Complexity: O(1)