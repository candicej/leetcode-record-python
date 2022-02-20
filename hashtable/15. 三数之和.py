class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        # 存储最终返回结果
        res = []

        # i 的取值一共是 n - 2种
        for i in range(0, n - 2):
            # 如果是第一个就大于 0 那么不可能总和等于0
            if nums[i] > 0:
                break

            # 如果nums[i]和前一个数相同 就不进行循环了 ，因为已经将 nums[i - 1] 的所有组合加入到结果中，本次双指针搜索只会得到重复组合。
            # 去重i：和为 0 且不重复的三元组。这一步很关键，不然就会重复
            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            # 定义左右指针
            l = i + 1
            r = n - 1

            # 当左指针小于右指针时，才遍历
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # 去重l
                    while (l < r and nums[l+1] == nums[l]):
                        l = l + 1
                    # 去重r
                    while (l < r and nums[r-1] == nums[r]):
                        r = r - 1
                    # 没有重复的之后，左右指针各自移动一步
                    l = l + 1
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                else:
                    l = l + 1
        return res
