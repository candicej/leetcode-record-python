# 双指针法 但是这个方法不能ac，因为遇到有相同前缀的情况会错误匹配
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         i = 0
#         for j in range(len(s)+1):
#             if s[i:j] in wordDict:
#                 i = j
#         if i==j:
#             return True
#         else:
#             return False

# 动态规划法
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        # 在dp表最前面加了一个
        dp=[False]*(n+1)
        dp[0]=True
        # 需要对每个i都判断
        for i in range(n):
            for j in range(i+1,n+1):
                # 只有当dp[i] =true前面的都符合在看当前的有没有
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]