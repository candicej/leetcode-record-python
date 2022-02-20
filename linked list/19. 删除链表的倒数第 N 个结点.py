class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #创建哑巴节点
        dummy = ListNode(-1)
        dummy.next = head
        # 快慢指针，慢的那个是dummy,这样就会返回被删的节点的前一个节点
        slow,fast = dummy, head
        # 快指针先走
        while n:
            fast = fast.next
            n -= 1
        # 当 fast 为空时候， slow正好走到被删的节点的前一个
        while fast:
            slow = slow.next
            fast = fast.next
        # 删掉节点
        slow.next = slow.next.next
        # 不能用return head， 因为可能存在链表元素只有一个的情况
        return dummy.next