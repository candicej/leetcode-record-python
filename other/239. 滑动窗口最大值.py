from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 结果
        res = []
        # 创建一个双向队列
        # 队列的性质是 先进先出 尾部进，头部出
        # 这个窗口是向右滑动的，也就是说右边进，左边出，所以队列左边是头，右边是尾
        # 保证滑动窗口头部是最大值
        # deque存储的是index 而不是 元素值 存索引值方便判断最大值的索引是否在滑动窗口内
        que = deque()
        for i in range(n):
            # 当队列不为空，且新加入的元素比队首的值大，则将队列中所有元素出栈
            # que[-1] 是最右端的元素
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            # 是否是满足要求的索引
            # que[0] 最左端的
            if que and que[0] <= i-k:
                que.popleft()
            # 将元素入队
            que.append(i)
            # 这个是刚开始入队的时候，要已经有k个元素进去了
            if i >= k - 1:
                # q[0]为当前队列最大的值
                res.append(nums[que[0]])
        return res