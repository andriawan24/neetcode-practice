# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        res = ListNode()


        head = list1
        while head:
            arr.append(head.val)
            head = head.next

        head = list2
        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        temp = res
        for i in arr:
            item = ListNode(i)
            temp.next = item
            temp = temp.next

        return res.next