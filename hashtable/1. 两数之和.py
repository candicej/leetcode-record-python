class Solution:
    # 使用hash表，注意，哪个是键哪个是值，注意区分
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        for i, element in enumerate(nums):
            if target - element in res:
                return [i,res[target-element]]
            res[nums[i]] = i