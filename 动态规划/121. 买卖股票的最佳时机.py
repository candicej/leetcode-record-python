# 本质思想就是 利用原问题与子问题的关系，将其变成 大问题的解 = 小问题的解的函数， 
# 从而将问题变成size的扩展即可，当size到达最大后，原问题解决了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #赋初值
        dp = [0 for i in range(len(prices))]
        # 最小值
        min_val = prices[0]
        for i in range(1,len(prices)):
            # 更新最小值
            if prices[i] < min_val:
                min_val = prices[i]
                # 状态转移方程
            dp[i]  = max(dp[i-1], prices[i] - min_val)
        return dp[-1]