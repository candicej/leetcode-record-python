# 解法一 递归法
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root:TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        res = list()
        postorder(root)
        return res

# 解法二 迭代法  我不理解
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 到右节点为空的状态时，需要记录他的pre节点
        cur, pre = root, None
        stack, ans = [], []
        while cur or stack:
            # 找到最左节点
            while cur:
                stack.append(cur)
                cur = cur.left
            # 弹出元素
            cur = stack.pop()
            if not cur.right or cur.right == pre:
                ans.append(cur.val)
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right
        return ans
