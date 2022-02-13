# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        added = ListNode()
        current_node = added

        while (l1 and l2):

            if (l1.val <= l2.val):
                current_node.next = ListNode(val=l1.val)
                l1 = l1.next
                current_node = current_node.next

            elif (l2.val < l1.val):
                current_node.next = ListNode(val=l2.val)
                l2 = l2.next
                current_node = current_node.next

        while (l1):
            current_node.next = ListNode(val=l1.val)
            l1 = l1.next
            current_node = current_node.next

        while (l2):
            current_node.next = ListNode(val=l2.val)
            l2 = l2.next
            current_node = current_node.next

        return added.next
