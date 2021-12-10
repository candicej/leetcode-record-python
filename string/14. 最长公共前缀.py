class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果是空字符串 返回空
        if not strs:
            return " "
        n = len(strs)
        # 假设公共前缀是第一个字符串
        res = strs[0]
        # 对剩余的进行遍历
        for i in range(1,n):
            # 选长度短的那个
            l = min(len(res),len(strs[i]))
            j=0
            while j<l:
                # 如果不相等，就停止
                if strs[i][j] != res[j]:
                    break
                j += 1
            # 这时候，res[:j]
            res = res[:j]
            if not res:
                break
        return res