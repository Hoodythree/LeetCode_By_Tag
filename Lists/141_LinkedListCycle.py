# Linkedlist detectCircle1
def hasCycle(head):
        if not head or not head.next:
            return False
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Linkedlist detectCircle2
