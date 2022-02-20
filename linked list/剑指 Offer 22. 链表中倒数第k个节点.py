# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        while k:
            fast = fast.next
            k -= 1
        # 注意 fast 为空时停止， slow正好是倒数第n个节点
        while fast:
            slow = slow.next
            fast = fast.next
        return slow