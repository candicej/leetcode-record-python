# 方法一 直接比较反过来的字符串是否相等
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x

# 方法二 将整数的后半部分与前部分比较，为了防止溢出，只翻转前半部分
# 原始数字小于或等于反转后的数字时，就意味着我们已经处理了一半位数的数字了
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特例判断，如果是负数，就一定不是回文数 如果个位数是0也不是回文数
        if x<0 or (x%10==0 and x!=0):
            return False
        reverse = 0
        # 翻转
        while x>reverse:
            reverse = reverse*10 + x%10
            x = x//10
        # 奇数和偶数x == reverse 奇数就是revers//10 和x相等
        return x == reverse or x == reverse // 10