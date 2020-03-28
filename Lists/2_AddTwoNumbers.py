# Definition for singly-linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, nums):
        self.head = Node(0) if nums else None
        self.tail = self.head
        for n in nums:
            self.tail.next = Node(n)
            self.tail = self.tail.next

    def print_linkedlist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def add_node(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.head is None:
            self.head = data
        else:
            self.tail.next  = data
        self.tail = data

    def delete_node(self, index):
        curr = self.head
        counter = 1
        while (curr is not None) and counter < index - 1:
            curr = curr.next
            counter += 1
        temp = curr.next
        curr.next = temp.next


def addTwoNumbers(l1, l2):
    # create a new linkedlist
    head = tail = Node(0)
    carrier = 0
    while l1 or l2:
        if l1 and l2:
            curr = l1.data + l2.data + carrier
            new_node = Node(curr % 10)
            carrier = curr // 10
            tail.next = new_node
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        if not l1 and l2:
            curr = l2.data + carrier
            new_node = Node(curr % 10)
            carrier = curr // 10
            tail.next = new_node
            tail = tail.next
            l2 = l2.next
        if not l2 and l1:
            curr = l1.data + carrier
            new_node = Node(curr % 10)
            carrier = curr // 10
            tail.next = new_node
            tail = tail.next
            l1 = l1.next
    if carrier:
        tail.next = Node(carrier)
        tail = tail.next
    return head.next

def addTwoNumbers2(l1, l2):
    dummy = tail = Node(0)
    carrier = 0
    while l1 or l2 or carrier:
        curr = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carrier
        tail.next = Node(curr % 10)
        carrier = curr // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        tail = tail.next
    return dummy.next

def print_node(n):
    temp = n
    while temp:
        print(temp.data)
        temp = temp.next
    

        

if __name__ == '__main__':
    nums1 = [1, 3, 5]
    nums2 = [i for i in range(3, 6)]
    l1 = Linkedlist(nums1)
    l2 = Linkedlist(nums2)
    res = addTwoNumbers2(l1.head.next, l2.head.next)
    print_node(res)




