class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = max_right = 0
        for price in reversed(prices):
            max_right = max(max_right, price)
            max_profit = max(max_profit, max_right - price)
        return max_profit