# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 找中间节点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 画一个分别有4个和5个节点的链表就明白了
        # 节点个数为偶数时，fast就会为None
        # 是奇数的话，slow指针会刚好在中间那个位置，需要往后一个节点
        # 奇数时候，中点位置下一个，（这样翻转才一样）
        if fast:
            slow = slow.next

        # 迭代倒序链表
        # 注意这里不能给pre赋值
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        #  比较
        p1 = head
        p2 = pre
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True