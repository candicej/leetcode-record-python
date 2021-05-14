class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # 这里注意是返回n  不能是nums，因为返回类型必须是integer
        # 如果只有两个数，不用判断直接返回就行
        if n <2:
            return n

        # 双指针遍历
        i = 1
        for j in range(2, n):
            # 
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            # nums[j] == nums[i] 就需要判断
            else:
                if nums[j] != nums[i-1]:
                    i += 1
                    nums[i] = nums[j]
        
        # 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
        # 所以返回 i+1 可以返回前i个数
        return i+1
