# # 方法一 创建hash表 直接返回大于n/2的元素
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n =len(nums)
#         hashtable = dict()
#         for i in nums:
#             if i not in hashtable:
#                 hashtable[i] = 1
#             else:
#                 hashtable[i] += 1

#         for i in hashtable:
#             if hashtable[i] > n/2:
#                 return i

# # 也可以这么写 简洁一点
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dic = defaultdict(int)
#         #统计每个数字出现的次数
#         for num in nums:
#             dic[num] += 1
#         # 返回出现次数最多的num, 即返回字典中最大value对应的key
#         # 字典库函数，返回字典中最大value对应的key
#         return max(dic, key=dic.get)

# # 还可以这么写
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)


# 方法二 排序 中间的那个元素肯定是
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]