class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        # i 的取值一共是 n - 2种
        for i in range(0, n-2):
            # 如果是第一个就大于 0 那么不可能总和等于0 
            if nums[i] > 0:
                break

            # 如果nums[i]和前一个数相同 就不进行循环了 ，因为已经将 nums[i - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
            if (i>0 and nums[i] == nums[i-1]):
                continue
            
            # 定义左右指针
            l = i + 1
            r = n - 1
            # 当左指针小于右指针时，才遍历
            while (l < r):
                # 当 sum=0 的时候，将结果存放，然后要进行以i开头的，不同l，r组成的下一种可能
                if (nums[i] + nums[l] + nums[r] == 0):
                    res.append([nums[i], nums[l], nums[r]])
                    # 去重
                    while(l<r and nums[l]==nums[l+1]):
                        l=l+1
                    while(l<r and nums[r]==nums[r-1]):
                        r=r-1
                    # 没有重复的之后，左右指针各自移动一步
                    l = l + 1
                    r = r - 1
                # 如果sum>0 我们不需要考虑去重，直接移动版就完事了
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r = r - 1
                else:
                    l = l + 1
                    
        return res