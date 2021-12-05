# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 树的题先判断是否存在根节点
        if not root:
            return False
        # 然后 递归结束的条件 就是叶子节点
        if not root.left and not root.right:
            return root.val == targetSum
        # 函数的等价关系式子
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

