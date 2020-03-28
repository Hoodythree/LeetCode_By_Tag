# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
from LinkedList.LinkedListPkg import Linkedlist

def oddEvenList(head):
    if not head or not head.next:
            return head
    dummy_odd = odd_tail = ListNode(0)
    dummy_even = even_tail = ListNode(0)
    curr = head
    # insert at the end of linkedlist
    is_odd = 1
    while curr:
        if is_odd % 2 != 0:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:
            even_tail.next = curr
            even_tail = even_tail.next
        curr = curr.next
        is_odd += 1
    odd_tail.next = dummy_even.next
    even_tail.next = None
    return dummy_odd.next

nums = [1, 2, 3, 4]
l = Linkedlist(nums)
oddEvenList(l.head.next)

