# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# iteration
from LinkedList.LinkedListPkg import Node
from LinkedList.LinkedListPkg import Linkedlist

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy.next
    q = p.next
    while q:
        p.next = q.next
        q.next = dummy.next
        dummy.next = q
        q = p.next
    return dummy.next


def reverseList2(head):
    if not head or not head.next:
        return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p


def print_node(n):
    temp = n
    while temp:
        print(temp.data)
        temp = temp.next
nums = [1, 2, 3, 4, 5]
l = Linkedlist(nums)
print_node(reverseList2(l.head.next))