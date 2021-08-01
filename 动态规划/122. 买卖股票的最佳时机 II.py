class Solution:
    # 扫描一遍 只要后一天比前一天大 就把这两天的差值加一下
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res