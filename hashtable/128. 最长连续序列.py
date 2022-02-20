# 参考：https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 存储最长长度
        longest_length = 0
        # 将数组转化成hash集合，一方面可以去重，一方面用一个哈希表存储数组中的数，这样查看一个数是否存在即能优化至 O(1)O(1) 的时间复杂度
        nums_set = set(nums)
        # 开始遍历
        for num in nums_set:
            # 只有当这个数的前一个数不在数组里才开始遍历
            if num - 1 not in nums_set:
                current_num = num
                cur_length = 1
                # 遍历到最长的序列停止
                while current_num + 1 in nums_set:
                    cur_length += 1
                    current_num += 1
                longest_length = max(longest_length, cur_length)
        return longest_length



