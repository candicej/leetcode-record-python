# 方法一 hash集合
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        # 注意要用set() 因为只存了键，没有键值对，而且字典不能添加这个元素
        res = set()
        while head:
            if head in res:
                return head
            res.add(head)
            head = head.next
        return None

# 快慢指针法 这道题我自己是想不出来的，数学不好没办法
# 双指针法参考：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
