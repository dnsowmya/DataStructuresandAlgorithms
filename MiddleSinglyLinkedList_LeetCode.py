class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode):
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

# Create the linked lists and initialize using the constructor
list1 = ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(8)))))
list2 = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
# Call the function which returns the head node
new_obj = Solution()
print(new_obj.middleNode(list2).val)

# Time Complexity: O(n)
# Space Complexity: O(1)
