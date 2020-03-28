# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        carrier = 0
        head = None
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        while stack2 or stack1 or carrier:
            curr = (stack2.pop() if stack2 else 0) + \
            (stack1.pop() if stack1 else 0) + carrier
            carrier = curr // 10
            node = ListNode(curr % 10)
            node.next = head
            head = node
        return head
            