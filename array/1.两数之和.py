# 考察数组 hash表
class Solution:
    # 最简单的解法，暴力搜索，
    # 先遍历i，再遍历j 
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     for i in range (n):
    #         for j in range (i+1,n):
    #             if nums[i] + nums[j] == target:
    #                 return i,j

    # hash 表
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, element in enumerate(nums):
            # 寻找元素是否在hashtable中 节省时间
            if target - element in hashtable:
                return [hashtable[target - element], i]
            # 保存下标 
            hashtable[nums[i]] = i
