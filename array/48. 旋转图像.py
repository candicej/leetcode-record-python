# # 笨方法 使用辅助数组
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         # 几行 几列
#         m = len(matrix)
#         matrix1 = [[0] * m for _ in range(m)]
#         for i in range(m):
#             for j in range(m):
#                 matrix1[j][i] = matrix[m-i-1][j]
#         Python 这里不能 matrix = matrix1 因为是引用拷贝
#         引用拷贝 二者的引用是同一个对象，并没有创建出一个新的对象 因为是同一个对象的引用，所以两者改一个，另一个对象的值也随之改变
#         matrix[:] = matrix1


# 方法二 翻转代替旋转
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        # 首先水平翻转 
        for i in range(m // 2):
            for j in range(m):
                matrix[i][j], matrix[m - i - 1][j] = matrix[m - i - 1][j], matrix[i][j]

        # 然后中轴翻转
        for i in range(m):
            # 这里注意是 i 翻转上半部分
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]