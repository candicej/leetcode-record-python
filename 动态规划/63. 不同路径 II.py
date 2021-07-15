class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m是行数
        m = len(obstacleGrid)
        # n是列数
        n = len(obstacleGrid[0])
        # m行n列
        res = [[1 for _ in range(n)] for _ in range(m)]
        # 遍历 从左到右
        for j in range(n):
            for i in range(m):
                # 如果第一个格子就等于0，直接返回0
                if i==0 and j==0:
                    if obstacleGrid[i][j] == 1:
                        return 0
                #  判断边界条件 注意在边上的只要一个走不通了，下面的全都没法走
                elif i==0: 
                    if obstacleGrid[i][j] == 1 or res[i][j-1] == 0:
                        res[i][j] = 0
                elif j==0: 
                    if obstacleGrid[i][j] == 1 or res[i-1][j] ==0:
                        res[i][j] = 0
                # 中间格子的判断
                else:
                    if obstacleGrid[i][j] == 1:
                        res[i][j] = 0
                    # 状态转移方程
                    else:
                        res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]