# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方法一 递归法
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode):
            if not root:
                return
            # 先遍历左子树
            inorder(root.left)
            # 根节点
            res.append(root.val)
            # 遍历右子树
            inorder(root.right)

        res = list()
        inorder(root)
        return res


# 方法二 迭代法 使用一个固定的模板
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        # 都是要先把根节点压进去
        cur, stack = root, []
        # 只要当前节点或者栈有一个不是空就继续遍历
        while cur or stack:
            while cur:
                # cur 入栈
                stack.append(cur)
                # 找到当前最左端的孩子
                cur = cur.left
            # 弹出栈顶元素
            tmp = stack.pop()
            # 加入结果
            ans.append(tmp.val)
            # 弹出栈中叶节点的父节点，当左子树完全遍历完就会遍历右子树
            cur = tmp.right





