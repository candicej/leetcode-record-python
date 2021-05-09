# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 判断
        if not head or not head.next:
            return head

        # dummy 节点，也叫做 哑节点。
        # 它在链表的迭代写法中非常常见，因为对于本题而言，
        # 我们可能会删除头结点 head，为了维护一个不变的头节点，所以我们添加了 dummy，
        # 让dummy.next = head，这样即使 head 被删了，那么会操作 dummy.next 指向新的链表头部，
        # 所以最终返回的也是 dummy.next
        # 因为有可能会删掉头节点，所以创建一个dummy节点
        dummy = ListNode(0)
        dummy.next = head

        # 两个指针来判断是有相等的元素
        pre = dummy
        cur = head

        while cur and cur.next:
            # 如果有相等的元素 cur一直向后移动，停留在最后一个重复的元素
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            # 如果没有重复元素 pre直接向后移动一个
            if pre.next == cur:
                pre = pre.next 
            # 否则 pre指向cur.next
            else:
                pre.next = cur.next
            # 移动cur
            cur = cur.next
            
        return dummy.next
            