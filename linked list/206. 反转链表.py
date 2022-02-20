# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 方法一 递归
# 一看就是转换成头结点和除了头结点之外的链表两个问题
# 但是我不会啊，写不出来，递归还是不太理解
# 首先是递，将大问题转化为小问题
# 当只有一个节点的时候，不需要反转，以这个为节点进行归，完成反转
# 看一下这个 题解 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/


class Solution:
    # 拿test 1 2 3 4 5 当例子来说明
    def reverseList(self, head: ListNode) -> ListNode:
        # 结束条件
        # 只有当reverse 到节点5 时候 return 5
        if not head or not head.next:
            return head

        # node就是反转链表的头结点
        # 函数出栈过程中返回值p一直没有变，只是将当前函数的输入结点进行反转
        # node 为 reverse（5）时候返回的head 也就是5
        node = self.reverseList(head.next)
        # 反转
        # 执行reverse（4 5）
        # 这时候 head = 4
        head.next.next = head
        # 防止出现环
        # 在python中只存在None
        # 删除4->5 已经有了5->4 了
        head.next = None

        # node每次都是头节点5
        return node

# 执行reverseList(5),head节点为5处,返回5->null;
# 执行reverseList(4),head节点为4,从4节点的指针为4->5->null,执行head.next.next = head; head.next = null;后p节点的结果为5->4->null;
# 执行reverseList(3),head节点为3,从3节点的指针为3->4->null,[注意reverseList(4)只是改变了4和4节点后的地址互换，其之前的指针指向地址未变],执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->null;
# 执行reverseList(2),head节点为2,从2节点的指针为2->3->null,执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->2->null;
# 执行reverseList(1),head节点为1,从1节点的指针为1->2->null,执行head.next.next = head;head.next = null;后p节点的结果为5->4->3->2->1->null; 递归结束

# reverseList: head=1
#     reverseList: head=2
# 	    reverseList: head=3
# 		    reverseList:head=4
# 			    reverseList:head=5
# 					终止返回
# 				cur = 5
# 				4.next.next->4，即5->4
# 			cur=5
# 			3.next.next->3，即4->3
# 		cur = 5reverse
# 		2.next.next->2，即3->2
# 	cur = 5
# 	1.next.next->1，即2->1


# 迭代
# 还是参考 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 迭代真的很好理解！！一定要用迭代，就是用两个指针来遍历
# 我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
# 第二个指针 cur 指向 head，然后不断遍历 cur。
# 每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
# 都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 两个指针
        pre, cur = None, head
        # 注意边界是cur
        while cur:
            # 保存下一个节点
            tmp = cur.next
            # 开始翻转
            cur.next = pre
            # 往右遍历
            pre = cur
            cur = tmp
        # 最后的pre就是原先链表的最后一个元素了
        return pre




