# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# find where the circle starts
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        hasCircle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCircle = True
                break
        if hasCircle:
            while head != slow:
                head = head.next
                slow = slow.next
            return head
        else:
            return None
        