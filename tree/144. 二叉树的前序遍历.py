class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方法一 递归解法 前序后序中序都是相同的套路
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            # 结束条件：节点为null,则结束
            if not root:
                return
            # 遍历根节点
            res.append(root.val)
            # 遍历
            preorder(root.left)
            preorder(root.right)
        res = list()
        preorder(root)
        return res
# 时间复杂度：O(n)，其中 n 是二叉树的节点数。每一个节点恰好被遍历一次
# 空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(\log n)，最坏情况下树呈现链状，为 O(n)。


# 方法二 迭代解法
# 使用栈来递归
# https://www.bilibili.com/video/BV1dA411L7Mj  这个up讲得太好了！！！一下子明白了
# 1. 初始化栈，将根节点入栈
# 2. 当栈不为空时：
# 弹出栈顶元素 node，并将值添加到结果中；
# 如果 node 的右子树非空，将右子树入栈；
# 如果 node 的左子树非空，将左子树入栈

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 特例判断
        if not root:
            return
        # 把根节点压入栈中
        stack = [root]
        # 结果列表
        ans = []
        # 当栈不为空，也就是树还没遍历完
        while stack:
            # 弹出栈顶元素
            node = stack.pop()
            ans.append(node.val)
            # 先把右子树压进去，先进后出
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans



























