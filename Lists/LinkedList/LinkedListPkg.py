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
