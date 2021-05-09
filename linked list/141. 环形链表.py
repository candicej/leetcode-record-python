# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一 最简单 是遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过
# 创建一个hash表 
# 存入哈希表的是指针，不是节点的val，重复元素指针地址是不同的。所以就算有重复的val也不影响
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        link = set()
        # 遍历链表
        while head:
            if head in link:
                return True
            
            link.add(head)
            head = head.next
        return False

# 方法二 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	if  not head: return head
    	slow,fast = head, head.next
    	while fast and fast.next:
    		if fast == slow:
    			return True
    		slow = slow.next
    		fast = fast.next.next

    	return False
