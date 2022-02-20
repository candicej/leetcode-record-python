# 方法一 创建hash表
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        res = set()
        while headA:
            res.add(headA)
            headA = headA.next
        while headB:
            if headB in res:
                return headB
            headB = headB.next
        return None

# 方法二 进阶，不使用额外空间
# 不会做，不想做了哈哈哈