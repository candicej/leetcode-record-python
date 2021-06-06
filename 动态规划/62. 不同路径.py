class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 给dp表赋初值 默认是只有1条路
        dp = [[1 for _ in range(n)] for _ in range(m)]
        # 填表 从左到右 从上而下填表
        # 这里注意要从第2行第2列开始填，不然列表就会超出
        for j in range(1,n):
            for i in range(1,m):
                # 把左面的和上面的加起来就是当前路径之和
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    
        # 返回dp表的最后一个元素            
        return dp[m-1][n-1]

