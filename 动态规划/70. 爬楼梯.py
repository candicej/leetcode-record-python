# 暴力搜索 太垃圾了 我的锅 到后面的数值比较大的时候很难解决
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return 1
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# 可以用数组存储
# 自底向上DP
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0]*(n+1)
#         dp[0] = dp[1] = 1

#         for i in range(2,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[-1]
        
# 最优化的，可以只使用两个变量
# f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        for i in range(2,n+1):
            # 注意区分 二者的区别
            # b = a + b
            # a = b
            a, b = b, a+b
        
        return b