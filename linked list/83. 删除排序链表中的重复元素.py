# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 当 head 不存在或者 head.next 不存在，直接返回 head
        if not head or not head:
            return head

        cur = head

        # 当我们遍历到链表的最后一个节点时，cur.next 为空节点，如果不加以判断，访问 cur.next 对应的元素会产生运行错误。因此我们只需要遍历到链表的最后一个节点，而不需要遍历完整个链表。
        while cur.next:
            # 如果和当前值相同 断掉 
            if cur.next.val == cur.val:
                cur.next = cur.next.next
                
            # 否则向后移动
            else:
                cur = cur.next
        return head

