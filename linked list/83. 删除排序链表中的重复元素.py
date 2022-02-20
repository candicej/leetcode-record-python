# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 哑结点
        dummy = ListNode(0,head)
        if not head or not head.next:
            return head
        pre = dummy
        cur = head
        # 遍历结束条件 遍历到倒数第2个节点即停止
        while cur and cur.next:
            # 如果不重复，接着遍历
            if cur.val != cur.next.val:
                pre = pre.next
                cur = cur.next
            else:
                # 重复了 ，就删除前面的那个重复的节点，cur = 下一个节点
                pre.next = cur.next
                cur = cur.next
        return dummy.next