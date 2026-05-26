# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.reverse()

        new_head = ListNode(arr[0])
        curr = new_head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next

        return new_head