class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 特例判断
        if n < 2:
            return s

        # 给dp表赋初值
        # dp[i][j] 表示 从i开始j结尾的字符串是否为回文串
        dp = [[False for _ in range(n)] for _ in range (n)]
        max_len = 1
        begin = 0

        # 从左到右 从上到下填表
        for j in range(1,n):
            for i in range (0,j):
                # 如果最左边和最右边的字符相等
                if s[i] == s[j]:
                    # 当 j-1 -(i+1) < 1 即j - i<3的时候，肯定是回文
                    if j - i < 3:
                        dp[i][j] = True
                    
                    else:
                        # 递归求解小问题
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                # 填完表之后，如果返回最长回文串，需要记录起始位置和最大长度
                if dp[i][j]:
                    # 最大长度
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        begin = i
        
        return s[begin:begin+max_len]
