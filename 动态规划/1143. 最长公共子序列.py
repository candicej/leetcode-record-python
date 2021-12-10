"""
给定两个字符串text1 和ext2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列

"""
# 动态规划经典 二维的
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 求出数组长度
        m = len(text1)
        n = len(text2)
        # 创建一个m+1 行 n+1 列的二维数组  默认为0
        dp = [[0] * (n+1) for _ in range(m+1)]
        # 按照行主次序计算表项 从左到右计算dp的第一行，然后计算第二行
        # 自底向上
        for i in range(1,m+1):
            for j in range(1,n+1):
                # 如果相等
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # 不等
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]