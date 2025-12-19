class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in reversed(range(len(prices) - 1)):
            max_profit += max(0, prices[i + 1] - prices[i])
        return max_profit