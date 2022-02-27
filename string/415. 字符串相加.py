# 模拟法 从右到左相加
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ''
        # 注意 要用while 循环，如果用for循环，那么不好补0，跟链表那道题不一样，因为num[i] 如果越界就会报错，链表是为空
        while i>=0 or j>=0:
            a = int(num1[i]) if i>=0 else 0
            b = int(num2[j]) if j>=0 else 0
            ans = a+b+carry
            carry = 1 if ans >9 else 0
            res = str(ans%10) + res
            i -= 1
            j -= 1
        if carry>0:
            # 字符串的加法
            res = str(1) + res
        return res