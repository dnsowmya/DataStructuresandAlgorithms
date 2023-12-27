class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, linkedlist):

        unique_set = set()
        dummy = ListNode(-1)
        dummy.next = linkedlist
        current_node = linkedlist
        prev = dummy
        unique_set.add(dummy.next)
        while current_node:
            if current_node.val in unique_set:
                prev.next = current_node.next
                current_node = current_node.next
            else:
                unique_set.add(current_node.val)
                prev = current_node
                current_node = current_node.next

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
dedupresult = new_obj.deleteDuplicates(newlinkedlist)
print_result_dedup = print_linkedlist.print_output_method(dedupresult)
print(print_result_dedup)

# Time Complexity: O(n)
# Space Complexity: O(n)

