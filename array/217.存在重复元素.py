# # 方法一 先排序 然后遍历一遍 判断有无相同元素
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(0,len(nums)-1):
#             if nums[i+1] == nums[i]:
#                 return True
#         return False
    
# # 方法二 使用hash表 比较普通的方法
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashtable = defaultdict(int)
#         for num in nums:
#             hashtable[num] += 1
#             if hashtable.get(num) >1:
#                 return True
#                 break
#         return False  

# 换一种写法
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Hash  = {}
        for i in nums:
            Hash[i] = Hash.get(i,0) + 1
            if Hash.get(i) > 1:
                return True 
                break
        return  False