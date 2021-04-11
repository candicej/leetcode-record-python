# 方法一 ，最普通的，遍历每一位，直接加
class Solution:
    def plusOne(self, digits:List[int]) ->List[int]:
        # 从数组最后一个坐标开始遍历，到0结束，所以结束坐标是-1，倒着遍历，所以是-1
        for i in range(len(digits)-1, -1,-1 ):
            # 如果不进位的话
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                # 如果digits第0个坐标是0，那么在首位插入一个1
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits



# 方法二 ：先将数组转化成数字，加1之后再转化为数组
class Solution:
	def plusOne(self, digits:List[int]) ->List[int]:
		nums_str = ""
		# 先将数组转化为字符串
		for i in digits:
			nums_str = nums_str + str(i)

		# 字符串转化为整数
		nums_int = int(nums_str) + 1

		# 将数字转化为数组
		res = []
		for i in str(nums_int):
            # 将字符串转化数组
            # 数组添加是 append
			res.append(int(i))
		return res
