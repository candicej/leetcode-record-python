class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 0
        r = x
        while l<=r:
            mid = (l+r)//2
            # 保证严格小于
            if mid*mid <= x and (mid+1)*(mid+1)>x:
                return mid
            # 大于
            elif mid*mid > x:
                r = mid -1
            # 小于但还不是最小的那个
            elif mid*mid <= x and (mid+1)*(mid+1)<=x:
                l = mid + 1
        return mid 