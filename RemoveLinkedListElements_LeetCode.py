class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # TODO
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy.next
        prev = dummy
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next

class Output:

    def print_output_method(self, head):
        result = ""
        while head is not None:
            result += str(head.val)
            head = head.next
            if head is not None:
                result += "->"
        return result

newlinkedlist = ListNode(1, ListNode(1, ListNode(2, ListNode(3))))
print_linkedlist = Output()
print_result = print_linkedlist.print_output_method(newlinkedlist)
print(print_result)

new_obj = Solution()
dedupresult = new_obj.removeElements(newlinkedlist, 1)
print_result_dedup = print_linkedlist.print_output_method(dedupresult)
print(print_result_dedup)