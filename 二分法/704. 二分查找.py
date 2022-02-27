class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) -1
        # 注意 这里必须是= 不然当l=r 时会漏掉一个元素
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid +1
            else:
                r = mid -1
        return -1