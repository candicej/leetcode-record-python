# # 方法一 借助set来相减，方法比较笨，不推荐
# # 可以在 O(N)的时间和 O(N) 的空间内解决
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         # 集合保证元素无重复，因此计算集合中的所有元素之和的两倍
#         return (3*sum(set(nums)) - sum(nums))//2


# # 方法二
# # 利用hashmap统计每个元素出现的次数
# from collections import Counter
# class Solution:
#     def singleNumber(self, nums):
#         hashmap = Counter(nums)
            
#         for k in hashmap.keys():
#             if hashmap[k] == 1:
#                 return k


# 进阶解法 不使用额外空间
# 方法三 不是我自己想出来的 我也不是很懂 待研究 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
# 链接：https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
