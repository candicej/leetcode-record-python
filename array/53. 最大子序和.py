# 方法一：贪心算法
# 贪心算法在求解某个问题时，总是做出眼前的最大利益，也就是说只顾眼前不顾大局，所以他是局部最优解
# 心策略必须具备无后效性，即某个状态以前的状态不会影响以后的状态，只与当前状态有关
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	n = len(nums)

    	for i in range(0, n-1):
    		# 用nums[i]来存储前i个元素的和
    		# 如果前面i个数的和大于0 我们就要着他，否则我们就不要他
    		if nums[i] > 0:
    			nums[i+1] += nums[i]

    	return max(nums)


# 方法二： 动态规划
# 后面会补全 现在重点不是动态规划


# 方法三：分治法，比较难我先不考虑