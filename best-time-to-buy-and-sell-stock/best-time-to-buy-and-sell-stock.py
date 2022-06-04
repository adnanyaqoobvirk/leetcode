class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            profit = max(profit, price - min_price)
            if price < min_price:
                min_price = price
        return profit