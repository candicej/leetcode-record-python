class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        # 难点在于flag
        flag = 0

        # 用来存储最后一个单词的长度
        count = 0
        # 倒着遍历
        for i in range(n-1, -1, -1):
            # 只有当遍历到第一个不是空格的时候我们才开始计数
            if s[i] != " ":
                flag = 1
                count += 1
            # 如果flag= 1 并且出现了空格，那么返回count就可以
            if flag and s[i] == " ":
                return count

        # 没出现过空格，直接返回count
        return count
