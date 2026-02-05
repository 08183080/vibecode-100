class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 999999999999
        b = 0
        for price in prices:
            if price < a:
                a = price
            temp = price - a
            if temp > b:
                b = temp
        return b