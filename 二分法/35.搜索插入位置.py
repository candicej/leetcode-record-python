# 方法一 ，直接遍历 遇到第一个比自己小的直接插在他的前面
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0,n):
            # 找到第一个大于等于target的值 返回
            if target <= nums[i]:
                return i
        return n



# 方法二 ，考虑到是有序数组，所以可以是使用二分法来缩短查找时间
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	n = len(nums)
    	l,r = 0, n-1

    	# 特殊判断 也就是不存在大于target的值
    	if nums[n-1] < target:
    		return n

        # 找出第一个大于等于 target 的元素的位置，那么小于 target 的元素就一定不是我们要找的解
    	# 确保target<=nums[len-1]
    	while l<r:
    		# 中间元素的坐标
    		m = l + (r - l)//2
            
            # if语句写容易判断的
    		# 下一轮搜索区间是 [mid + 1..right]
    		if nums[m] < target:
    			l = m + 1
    		# 因为不在右边区间了，那么就在左边找，保持区间的完整性
    		else:
    			r = m 
    	return l

