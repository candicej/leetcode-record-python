# 利用位运算 不适用额外空间 利用性质a^a = 0 a^0 =a
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a =0
        for num in nums:
            a = a ^ num
        return a
    # 如果想节省空间 可以不借助a
    # nums[0] ^= nums[i] 就可以了  