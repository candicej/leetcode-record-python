# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 处理两个链表 主要涉及新建一个链表，关键是赋值需要cur = ListNode(val) !!!!!!!!!!!!注意
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0

        while l1 or l2:
            # 避免 长度不一样的情况 补0
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            sum = x1 + x2 + carry
            cur.next = ListNode(sum % 10)
            # 进位
            carry = 1 if sum > 9 else 0

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 最后有进位，需要加一
        if carry:
            cur.next = ListNode(1)
        return dummy.next
