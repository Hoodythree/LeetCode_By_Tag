from LinkedList.LinkedListPkg import Node
from LinkedList.LinkedListPkg import Linkedlist

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_node(n):
    temp = n
    while temp:
        print(temp.data)
        temp = temp.next

def deleteDuplicates(head):
        if not head or not head.next:
            return head
        p = head
        q = head.next
        while q:
            while q and q.data == p.data:
                q = q.next
            if q:
                p.next = q
                p = p.next
                q = q.next
        p.next = q
        return head

def nextLargerNodes(head):
        res = []
        curr = head
        while curr:
            temp = curr.next
            while temp:
                if temp.data > curr.data:
                    res.append(temp.data)
                    break
                else:
                    temp = temp.next
            if not temp:
                res.append(0)
            curr = curr.next
        return res

nums = [1, 1, 2, 2]
l = Linkedlist(nums)
print(nextLargerNodes(l.head.next))