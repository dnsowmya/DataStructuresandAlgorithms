# Definition for Singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

# Create the linked lists and initialize using the constructor
head = ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(8)))))
list2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

# Call the function which returns the head node
new_obj = Solution()
print(new_obj.isPalindrome(list2))
