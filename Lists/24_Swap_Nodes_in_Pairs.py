from LinkedList.LinkedListPkg import Node
from LinkedList.LinkedListPkg import Linkedlist

# https://github.com/MisterBooo/LeetCodeAnimation
# pre -> node1 -> node2 -> next
def swapPairs(head):
    if not head:
        return
    # use dummy to track Linkedlist
    # dummy -> head
    dummy = Node(0)
    dummy.next = head
    pre = dummy
    node1 = pre.next
    node2 = node1.next if node1 else None
    next = node2.next if node2 else None
    # do while loop when node2 is not None
    # 这是为了不让只有一个元素的链表执行循环
    # 如果使用next不为空的话，则两个元素的链表无法执行循环
    while node2:
        node2.next = node1
        node1.next = next
        pre.next = node2
        pre = node1
        node1 = next if next else None
        node2 = node1.next if node1 else None
        next = node2.next if node2 else None
    return dummy.next

# improvement version
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
# three pointers
        node1 = pre.next
        node2 = node1.next
        next = node2.next
# swap
        node2.next = node1
        node1.next = next
        pre.next = node2
        pre = node1
    return dummy.next





def print_node(n):
    temp = n
    while temp:
        print(temp.data)
        temp = temp.next
nums = [1, 2]
l = Linkedlist(nums)
print_node(swapPairs(l.head.next))

