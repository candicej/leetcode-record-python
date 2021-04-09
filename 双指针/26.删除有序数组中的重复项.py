# 双指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


# 考虑用 2 个指针，一个在前记作 p，一个在后记作 q，算法流程如下：
# 1.比较 p 和 q 位置的元素是否相等。
# 如果相等，q 后移 1 位
# 如果不相等，将 q 位置的元素复制到 p+1 位置上，p 后移一位，q 后移 1 位
# 重复上述过程，直到 q 等于数组长度。
# 返回 p + 1，即为新数组长度。

