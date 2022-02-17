# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一 递归
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 参考：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            # 递归向上返回结果的部分
            # 每一个递归都要有返回值的 ！！！！！！！！！！！！
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# 关于return List1的理解: 递归的核心在于,我只关注我这一层要干什么,返回什么,至于我的下一层(规模减1),我不管,我就是甩手掌柜.
#
# 好,现在我要merge L1,L2.我要怎么做?
#
# 显然,如果L1空或L2空,我直接返回L1或L2就行,这很好理解.
# 如果L1第一个元素小于L2的? 那我得把L1的这个元素放到最前面,至于后面的那串长啥样 ,我不管. 我只要接过下级员工干完活后给我的包裹, 然后把我干的活附上去(令L1->next = 这个包裹)就行
# 这个包裹是下级员工干的活,即merge(L1->next, L2)
# 我该返回啥?
#
# 现在不管我的下一层干了什么,又返回了什么给我, 我只要知道,假设我的工具人们都完成了任务, 那我的任务也就完成了,可以返回最终结果了
# 最终结果就是我一开始接手的L1头结点+下级员工给我的大包裹,要一并交上去, 这样我的boss才能根据我给它的L1头节点往下找,检查我完成的工作

# 方法二 迭代
# 使用递归的一般都可以使用迭代，空间复杂度也更小 先不考虑 以后回来解题
