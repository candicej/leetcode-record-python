# 我的想法是借助一个辅助数组来记录矩阵是否被访问过 但是内存消耗有点大 而且我也没写出来
# 可以维护四个边界 l1,l2,r1,r2 分别代表左上边界、左下边界、右上边界、右下边界 ，每次遍历一层 然后修改边界 从而更改循环范围
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # 左右上下边界
        left, right, top, bottom = 0, n-1, 0, m-1
        # 存储结果
        res = []

        # 结束条件
        while len(res) < m*n:
            # 在顶层 从做到有遍历
            for i in range(left, right+1):
                res.append(matrix[top][i])
            # 在最右边 从上到下遍历
            for j in range(top+1, bottom+1):
                res.append(matrix[j][right])
            if left < right and top < bottom:
                # 在底层 从右到左遍历
                for j in range(right-1, left,-1):
                    res.append(matrix[bottom][j])
                # 在最左边 从下到上遍历
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            # 更改四个边界的值
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom -1

        return res