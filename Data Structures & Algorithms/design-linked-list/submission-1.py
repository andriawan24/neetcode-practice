class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next

        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        cur = self.head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next
        self.size -= 1