# 最简单的方法，使用hash集合来记录是否出现过，不是用hashtable
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        # 注意要用set() 因为只存了键，没有键值对，而且字典不能添加这个元素
        res = set()
        while head:
            if head in res:
                return True
            res.add(head)
            head = head.next
        return False

# 方法二 快慢指针 不使用额外的空间
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False