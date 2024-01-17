# Definition for Singly Linked List
# class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solutuion:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1