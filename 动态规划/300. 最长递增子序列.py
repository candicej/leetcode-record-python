# 参考https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
# 我就是傻逼，好难，哈哈哈哈
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 存储长度
        dp = []
        # dp[i] 存储的是以i结尾的最长严格递增序列的长度
        # 遍历每一个数
        for i in range(len(nums)):
            # 初始的就是1
            dp.append(1)
            # 对于i,遍历每一个它前面的数，看看有没有比他小的
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)