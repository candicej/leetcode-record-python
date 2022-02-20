# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 哑结点
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        while cur and cur.next:
            # 如果有重复，一直移动 ！！！！注意：这个地方要加一个while cur.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 没有重复元素
            if pre.next == cur:
                # 直接移动 遍历下一个
                pre = pre.next
                cur = cur.next
            # 有重复元素
            else:
                # cur 移动到没有重复的元素
                cur = cur.next
                # 重新指向 pre指向没有重复的元素
                pre.next = cur
        return dummy.next
