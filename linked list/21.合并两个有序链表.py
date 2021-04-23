# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 方法一： 递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归停止的条件 边界条件
        if  not l1:
            return l2
        if not l2:
            return l1
        
        # 递归 需要叠加栈
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            # 这个地方不太理解
            return l1
        
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 方法二 迭代
# 使用递归的一般都可以使用迭代，空间复杂度也更小 先不考虑 以后回来解题