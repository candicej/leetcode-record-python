# Z 字形查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 行数
        m = len(matrix)
        # 列数
        n = len(matrix[0])
        # 从右上角的元素开始遍历！ 思路很巧妙 关键
        i,j = 0, n-1
        while i<m and j>=0:
            if target == matrix[i][j]:
                return True 
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False