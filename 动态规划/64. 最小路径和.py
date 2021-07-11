class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 创建二维数组 dp，与原始网格的大小相同，dp[i][j] 表示从左上角出发到 (i,j)(i,j) 位置的最小路径和。
        # dp[0][0]=grid[0][0]。对于dp 中的其余元素，通过以下状态转移方程计算元素值。
        res = [[0 for _ in range (n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                # 边界赋值
                if i ==0 and j == 0:
                    res[i][j] = grid[i][j]
                elif i == 0:
                    res[j][i] = res[j-1][i] + grid[j][i]
                elif j == 0:
                    res[j][i] = res[j][i-1] + grid[j][i]

                else:
                    res[j][i] = min(res[j-1][i],res[j][i-1]) + grid[j][i]
        return res[m-1][n-1]