# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy =ListNode(0)
        
        s, f = head, head
        while n:
            s = f.next
            n -= 1
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next 