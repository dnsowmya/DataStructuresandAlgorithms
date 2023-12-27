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
        
    def remove(self, index):
        if self.length == 0 or index < -1 or index > self.length-1 :
            return None
        if self.length == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None

        # if node to be removed is the head node
        elif index == 0:
            deleted_node = self.head
            self.head = deleted_node.next
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            deleted_node = temp_node.next

            # if node to be removed is the tail node
            if index == self.length - 1:
                self.tail = temp_node
                temp_node.next = None
            else:
                temp_node.next = deleted_node.next
        self.length -= 1
        return deleted_node
            

new_linked_list = LinkedList()
print(new_linked_list)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(f"{new_linked_list.remove(2).value} is deleted")
print(new_linked_list)
new_linked_list.remove(10)
print(new_linked_list)

# Time Complexity: O(n)
# Space Complexity: O(1)
