# Definition for a Single Linked List

class LinkedList(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = val

    def __str__(self):
        #temp_node = self.head
        print(self.head)
        print(self.next)

class Solution(object):
    def mergeTwoLists(self, l1, l2):

        prehead = LinkedList(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # If l1 and l2 are not of same length
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# Create the linked lists and initialize using the constructor
list1 = LinkedList(1, LinkedList(3, LinkedList(5, LinkedList(6, LinkedList(8)))))
list2 = LinkedList(2, LinkedList(3, LinkedList(4)))
# Call the function which returns the head node
new_obj = Solution()
head = new_obj.mergeTwoLists(list1, list2)
# Traverse the linked list and print each value
while head != None:
    print(head.val)
    head = head.next

# Time Complexity: O(1)
# Space Complexity: O(1)

