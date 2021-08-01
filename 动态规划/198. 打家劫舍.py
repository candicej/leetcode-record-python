# 解法一，内存占用比较大 新创一个dp表，可以但是没必要
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = [0 for i in range(len(nums))]
#         dp[0] = nums[0]
#         if len(nums)==1:
#             return dp[0]
#         dp[1] = max(nums[0],nums[1]) 
#         if len(nums) == 2:
#             return dp[1]
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-2]+nums[i], dp[i-1])  
#         return dp[-1]

# 解法二：直接原地修改
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 特例判断
        if len(nums)==1:
            return nums[0]
        # 特例判断：
        nums[1] = max(nums[0],nums[1]) 
        if len(nums) == 2:
            return nums[1]
        # 状态转移方程
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[-1]